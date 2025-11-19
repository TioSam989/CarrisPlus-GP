"""
User model and database operations
"""
import bcrypt
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
