"""
Authentication routes for login and registration
"""
from flask import Blueprint, request, jsonify
from models.user import User
from auth.utils import (
    generate_token, validate_email, validate_password,
    validate_nif, sanitize_input, token_required
)
from config.database import get_db_cursor
from datetime import datetime


auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Register a new user

    Request JSON:
        {
            "email": "user@example.com",
            "password": "SecurePass123",
            "nif": "123456789",
            "full_name": "John Doe",
            "phone": "+351912345678" (optional)
        }

    Returns:
        201: User created successfully with token
        400: Validation error
        409: User already exists
        500: Server error
    """
    try:
        print("=== REGISTER REQUEST START ===")
        data = request.get_json()
        print(f"Request data received: {data}")

        # Extract and sanitize inputs
        email = sanitize_input(data.get('email', '').lower().strip())
        password = data.get('password', '')
        nif = sanitize_input(data.get('nif', '').strip())
        full_name = sanitize_input(data.get('full_name', '').strip())
        phone = sanitize_input(data.get('phone', '').strip()) if data.get('phone') else None

        print(f"Sanitized - Email: {email}, NIF: {nif}, Name: {full_name}, Phone: {phone}")

        # Validate required fields
        if not all([email, password, nif, full_name]):
            print(f"❌ Missing required fields")
            return jsonify({
                'error': 'Missing required fields',
                'required': ['email', 'password', 'nif', 'full_name']
            }), 400

        print("✅ All required fields present")

        # Validate email
        if not validate_email(email):
            print(f"❌ Invalid email format: {email}")
            return jsonify({'error': 'Invalid email format'}), 400
        print("✅ Email format valid")

        # Validate password
        is_valid_password, password_error = validate_password(password)
        if not is_valid_password:
            print(f"❌ Password validation failed: {password_error}")
            return jsonify({'error': password_error}), 400
        print("✅ Password valid")

        # Validate NIF
        is_valid_nif, nif_error = validate_nif(nif)
        if not is_valid_nif:
            print(f"❌ NIF validation failed: {nif_error}")
            return jsonify({'error': nif_error}), 400
        print("✅ NIF valid")

        # Check if user already exists
        print(f"Checking if email exists: {email}")
        existing_user = User.get_user_by_email(email)
        if existing_user:
            print(f"❌ Email already registered: {email}")
            return jsonify({'error': 'Email already registered'}), 409
        print("✅ Email not registered yet")

        # Check if NIF already exists
        print(f"Checking if NIF exists: {nif}")
        with get_db_cursor() as cursor:
            cursor.execute('SELECT id FROM users WHERE nif = %s', (nif,))
            if cursor.fetchone():
                print(f"❌ NIF already registered: {nif}")
                return jsonify({'error': 'NIF already registered'}), 409
        print("✅ NIF not registered yet")

        # Create user
        print(f"Creating user: {email}")
        user = User.create_user(email, password, nif, full_name, phone)

        if not user:
            print("❌ Failed to create user in database")
            return jsonify({'error': 'Failed to create user'}), 500

        print(f"✅ User created successfully with ID: {user.get('id')}")

        # Generate JWT token
        token = generate_token(user['id'], user['email'], user['is_admin'])

        # Log registration
        log_audit(user['id'], 'USER_REGISTERED', 'user', user['id'], request)

        return jsonify({
            'message': 'User registered successfully',
            'token': token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'full_name': user['full_name'],
                'nif': user['nif'],
                'phone': user['phone'],
                'is_admin': user['is_admin']
            }
        }), 201

    except Exception as e:
        print(f"❌ REGISTRATION ERROR: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login user

    Request JSON:
        {
            "email": "user@example.com",
            "password": "SecurePass123"
        }

    Returns:
        200: Login successful with token
        400: Validation error
        401: Invalid credentials
        403: Account locked
        500: Server error
    """
    try:
        data = request.get_json()

        # Extract and sanitize inputs
        email = sanitize_input(data.get('email', '').lower().strip())
        password = data.get('password', '')

        # Validate required fields
        if not all([email, password]):
            return jsonify({
                'error': 'Missing required fields',
                'required': ['email', 'password']
            }), 400

        # Get user by email
        user = User.get_user_by_email(email)

        if not user:
            return jsonify({'error': 'Invalid email or password'}), 401

        # Check if account is locked
        if User.is_account_locked(user):
            locked_until = user['locked_until'].strftime('%Y-%m-%d %H:%M:%S')
            return jsonify({
                'error': 'Account is temporarily locked due to multiple failed login attempts',
                'locked_until': locked_until
            }), 403

        # Check if account is active
        if not user['is_active']:
            return jsonify({'error': 'Account is deactivated'}), 403

        # Verify password
        if not User.verify_password(password, user['password_hash']):
            # Increment failed attempts
            User.increment_failed_attempts(email)

            # Log failed login
            log_audit(user['id'], 'LOGIN_FAILED', 'user', user['id'], request)

            return jsonify({'error': 'Invalid email or password'}), 401

        # Reset failed attempts on successful login
        User.reset_failed_attempts(email)

        # Generate JWT token
        token = generate_token(user['id'], user['email'], user['is_admin'])

        # Log successful login
        log_audit(user['id'], 'LOGIN_SUCCESS', 'user', user['id'], request)

        return jsonify({
            'message': 'Login successful',
            'token': token,
            'user': {
                'id': user['id'],
                'email': user['email'],
                'full_name': user['full_name'],
                'nif': user['nif'],
                'phone': user['phone'],
                'is_admin': user['is_admin']
            }
        }), 200

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@auth_bp.route('/me', methods=['GET'])
@token_required
def get_current_user(current_user):
    """
    Get current logged-in user information

    Headers:
        Authorization: Bearer <token>

    Returns:
        200: User information
        401: Unauthorized
    """
    try:
        user = User.get_user_by_id(current_user['user_id'])

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'user': {
                'id': user['id'],
                'email': user['email'],
                'full_name': user['full_name'],
                'nif': user['nif'],
                'phone': user['phone'],
                'is_admin': user['is_admin'],
                'created_at': user['created_at'].isoformat() if user['created_at'] else None
            }
        }), 200

    except Exception as e:
        print(f"Get user error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@auth_bp.route('/logout', methods=['POST'])
@token_required
def logout(current_user):
    """
    Logout user (client-side token removal)

    Headers:
        Authorization: Bearer <token>

    Returns:
        200: Logout successful
    """
    try:
        # Log logout action
        log_audit(current_user['user_id'], 'LOGOUT', 'user', current_user['user_id'], request)

        return jsonify({'message': 'Logout successful'}), 200

    except Exception as e:
        print(f"Logout error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@auth_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    """
    Request password reset

    Request JSON:
        {
            "email": "user@example.com"
        }

    Returns:
        200: Reset email sent (always returns success for security)
        400: Validation error
        500: Server error
    """
    try:
        data = request.get_json()

        # Extract and sanitize email
        email = sanitize_input(data.get('email', '').lower().strip())

        # Validate email
        if not email or not validate_email(email):
            return jsonify({'error': 'Valid email is required'}), 400

        # Create reset token (always return success even if user doesn't exist for security)
        token = User.create_password_reset_token(email)

        if token:
            # In production, send email here with reset link
            # For now, we'll return the token in the response (NOT SECURE FOR PRODUCTION)
            # TODO: Implement email sending
            reset_link = f"http://localhost:3000/reset-password?token={token}"
            print(f"Password reset link: {reset_link}")

            # Log password reset request
            user = User.get_user_by_email(email)
            if user:
                log_audit(user['id'], 'PASSWORD_RESET_REQUESTED', 'user', user['id'], request)

        # Always return success message for security (don't reveal if email exists)
        return jsonify({
            'message': 'If an account exists with this email, you will receive password reset instructions.',
            'reset_link': reset_link if token else None  # Remove this in production
        }), 200

    except Exception as e:
        print(f"Forgot password error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    """
    Reset password using token

    Request JSON:
        {
            "token": "reset_token_here",
            "password": "NewSecurePass123"
        }

    Returns:
        200: Password reset successful
        400: Validation error
        401: Invalid or expired token
        500: Server error
    """
    try:
        data = request.get_json()

        # Extract inputs
        token = data.get('token', '').strip()
        password = data.get('password', '')

        # Validate required fields
        if not token or not password:
            return jsonify({
                'error': 'Missing required fields',
                'required': ['token', 'password']
            }), 400

        # Validate password
        is_valid_password, password_error = validate_password(password)
        if not is_valid_password:
            return jsonify({'error': password_error}), 400

        # Verify token and get user
        token_data = User.verify_reset_token(token)
        if not token_data:
            return jsonify({'error': 'Invalid or expired reset token'}), 401

        # Reset password
        if User.reset_password(token, password):
            # Log password reset
            log_audit(token_data['user_id'], 'PASSWORD_RESET_COMPLETED', 'user', token_data['user_id'], request)

            return jsonify({
                'message': 'Password has been reset successfully. You can now login with your new password.'
            }), 200
        else:
            return jsonify({'error': 'Failed to reset password'}), 500

    except Exception as e:
        print(f"Reset password error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@auth_bp.route('/verify-reset-token', methods=['POST'])
def verify_reset_token():
    """
    Verify if a reset token is valid

    Request JSON:
        {
            "token": "reset_token_here"
        }

    Returns:
        200: Token is valid
        400: Validation error
        401: Invalid or expired token
    """
    try:
        data = request.get_json()
        token = data.get('token', '').strip()

        if not token:
            return jsonify({'error': 'Token is required'}), 400

        token_data = User.verify_reset_token(token)
        if token_data:
            return jsonify({
                'valid': True,
                'email': token_data['email']
            }), 200
        else:
            return jsonify({'error': 'Invalid or expired reset token'}), 401

    except Exception as e:
        print(f"Verify token error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


def log_audit(user_id, action, entity_type, entity_id, req):
    """
    Log audit event

    Args:
        user_id: User ID performing the action
        action: Action name
        entity_type: Type of entity (e.g., 'user', 'document')
        entity_id: ID of the entity
        req: Flask request object
    """
    try:
        ip_address = req.remote_addr
        user_agent = req.headers.get('User-Agent', '')

        with get_db_cursor(commit=True) as cursor:
            cursor.execute('''
                INSERT INTO audit_logs (user_id, action, entity_type, entity_id, ip_address, user_agent)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (user_id, action, entity_type, entity_id, ip_address, user_agent))

    except Exception as e:
        print(f"Audit log error: {e}")
