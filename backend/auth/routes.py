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
        data = request.get_json()

        # Extract and sanitize inputs
        email = sanitize_input(data.get('email', '').lower().strip())
        password = data.get('password', '')
        nif = sanitize_input(data.get('nif', '').strip())
        full_name = sanitize_input(data.get('full_name', '').strip())
        phone = sanitize_input(data.get('phone', '').strip()) if data.get('phone') else None

        # Validate required fields
        if not all([email, password, nif, full_name]):
            return jsonify({
                'error': 'Missing required fields',
                'required': ['email', 'password', 'nif', 'full_name']
            }), 400

        # Validate email
        if not validate_email(email):
            return jsonify({'error': 'Invalid email format'}), 400

        # Validate password
        is_valid_password, password_error = validate_password(password)
        if not is_valid_password:
            return jsonify({'error': password_error}), 400

        # Validate NIF
        is_valid_nif, nif_error = validate_nif(nif)
        if not is_valid_nif:
            return jsonify({'error': nif_error}), 400

        # Check if user already exists
        existing_user = User.get_user_by_email(email)
        if existing_user:
            return jsonify({'error': 'Email already registered'}), 409

        # Check if NIF already exists
        with get_db_cursor() as cursor:
            cursor.execute('SELECT id FROM users WHERE nif = %s', (nif,))
            if cursor.fetchone():
                return jsonify({'error': 'NIF already registered'}), 409

        # Create user
        user = User.create_user(email, password, nif, full_name, phone)

        if not user:
            return jsonify({'error': 'Failed to create user'}), 500

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
        print(f"Registration error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


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
