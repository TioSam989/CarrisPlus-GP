"""
User model and database operations
"""
import bcrypt
import secrets
from config.database import get_db_cursor
from datetime import datetime, timedelta


class User:
    """User model for authentication and user management"""

    @staticmethod
    def hash_password(password):
        """Hash a password using bcrypt"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    @staticmethod
    def verify_password(password, password_hash):
        """Verify a password against its hash"""
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

    @staticmethod
    def create_user(email, password, nif, full_name, phone=None):
        """
        Create a new user

        Args:
            email: User email (unique)
            password: Plain text password
            nif: Portuguese NIF (9 digits, unique)
            full_name: User's full name
            phone: Optional phone number

        Returns:
            dict: Created user data (without password)
            None: If user creation fails
        """
        try:
            password_hash = User.hash_password(password)

            with get_db_cursor(commit=True) as cursor:
                cursor.execute('''
                    INSERT INTO users (email, password_hash, nif, full_name, phone)
                    VALUES (%s, %s, %s, %s, %s)
                ''', (email, password_hash, nif, full_name, phone))

                user_id = cursor.lastrowid

                # Fetch and return the created user
                cursor.execute('''
                    SELECT id, email, nif, full_name, phone, created_at, is_active, is_admin
                    FROM users WHERE id = %s
                ''', (user_id,))

                return cursor.fetchone()

        except Exception as e:
            print(f"Error creating user: {e}")
            return None

    @staticmethod
    def get_user_by_email(email):
        """
        Get user by email

        Args:
            email: User email

        Returns:
            dict: User data
            None: If user not found
        """
        try:
            with get_db_cursor() as cursor:
                cursor.execute('''
                    SELECT id, email, password_hash, nif, full_name, phone,
                           created_at, is_active, is_admin, failed_login_attempts, locked_until
                    FROM users WHERE email = %s
                ''', (email,))

                return cursor.fetchone()

        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    @staticmethod
    def get_user_by_id(user_id):
        """
        Get user by ID

        Args:
            user_id: User ID

        Returns:
            dict: User data (without password)
            None: If user not found
        """
        try:
            with get_db_cursor() as cursor:
                cursor.execute('''
                    SELECT id, email, nif, full_name, phone,
                           created_at, is_active, is_admin
                    FROM users WHERE id = %s
                ''', (user_id,))

                return cursor.fetchone()

        except Exception as e:
            print(f"Error fetching user: {e}")
            return None

    @staticmethod
    def is_account_locked(user):
        """
        Check if user account is locked

        Args:
            user: User dictionary

        Returns:
            bool: True if locked, False otherwise
        """
        if user.get('locked_until'):
            return datetime.now() < user['locked_until']
        return False

    @staticmethod
    def increment_failed_attempts(email):
        """
        Increment failed login attempts and lock account if necessary

        Args:
            email: User email
        """
        try:
            with get_db_cursor(commit=True) as cursor:
                cursor.execute('''
                    UPDATE users
                    SET failed_login_attempts = failed_login_attempts + 1
                    WHERE email = %s
                ''', (email,))

                # Check if we need to lock the account (5 failed attempts)
                cursor.execute('''
                    SELECT failed_login_attempts FROM users WHERE email = %s
                ''', (email,))

                result = cursor.fetchone()
                if result and result['failed_login_attempts'] >= 5:
                    # Lock account for 15 minutes
                    lock_until = datetime.now() + timedelta(minutes=15)
                    cursor.execute('''
                        UPDATE users
                        SET locked_until = %s
                        WHERE email = %s
                    ''', (lock_until, email))

        except Exception as e:
            print(f"Error incrementing failed attempts: {e}")

    @staticmethod
    def reset_failed_attempts(email):
        """
        Reset failed login attempts on successful login

        Args:
            email: User email
        """
        try:
            with get_db_cursor(commit=True) as cursor:
                cursor.execute('''
                    UPDATE users
                    SET failed_login_attempts = 0, locked_until = NULL
                    WHERE email = %s
                ''', (email,))

        except Exception as e:
            print(f"Error resetting failed attempts: {e}")

    @staticmethod
    def create_password_reset_token(email):
        """
        Create a password reset token for a user

        Args:
            email: User email

        Returns:
            str: Reset token if successful
            None: If user not found or error occurs
        """
        try:
            user = User.get_user_by_email(email)
            if not user:
                return None

            # Generate a secure random token
            token = secrets.token_urlsafe(32)

            # Token expires in 1 hour
            expires_at = datetime.now() + timedelta(hours=1)

            with get_db_cursor(commit=True) as cursor:
                # Invalidate any existing tokens for this user
                cursor.execute('''
                    UPDATE password_reset_tokens
                    SET used = TRUE
                    WHERE user_id = %s AND used = FALSE
                ''', (user['id'],))

                # Create new token
                cursor.execute('''
                    INSERT INTO password_reset_tokens (user_id, token, expires_at)
                    VALUES (%s, %s, %s)
                ''', (user['id'], token, expires_at))

            return token

        except Exception as e:
            print(f"Error creating password reset token: {e}")
            return None

    @staticmethod
    def verify_reset_token(token):
        """
        Verify a password reset token

        Args:
            token: Reset token

        Returns:
            dict: User data if token is valid
            None: If token is invalid, expired, or used
        """
        try:
            with get_db_cursor() as cursor:
                cursor.execute('''
                    SELECT prt.*, u.id as user_id, u.email, u.full_name
                    FROM password_reset_tokens prt
                    JOIN users u ON prt.user_id = u.id
                    WHERE prt.token = %s AND prt.used = FALSE AND prt.expires_at > NOW()
                ''', (token,))

                return cursor.fetchone()

        except Exception as e:
            print(f"Error verifying reset token: {e}")
            return None

    @staticmethod
    def reset_password(token, new_password):
        """
        Reset user password using a valid token

        Args:
            token: Reset token
            new_password: New plain text password

        Returns:
            bool: True if password reset successful, False otherwise
        """
        try:
            token_data = User.verify_reset_token(token)
            if not token_data:
                return False

            # Hash the new password
            password_hash = User.hash_password(new_password)

            with get_db_cursor(commit=True) as cursor:
                # Update user password
                cursor.execute('''
                    UPDATE users
                    SET password_hash = %s, failed_login_attempts = 0, locked_until = NULL
                    WHERE id = %s
                ''', (password_hash, token_data['user_id']))

                # Mark token as used
                cursor.execute('''
                    UPDATE password_reset_tokens
                    SET used = TRUE
                    WHERE token = %s
                ''', (token,))

            return True

        except Exception as e:
            print(f"Error resetting password: {e}")
            return False
