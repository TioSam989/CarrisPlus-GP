"""
Authentication utilities for JWT and validation
"""
import jwt
import os
import re
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify


JWT_SECRET = os.getenv('JWT_SECRET_KEY', 'your-super-secret-jwt-key-change-in-production')
JWT_ALGORITHM = 'HS256'
JWT_EXP_HOURS = 24


def generate_token(user_id, email, is_admin=False):
    """
    Generate JWT token for user

    Args:
        user_id: User ID
        email: User email
        is_admin: Whether user is admin

    Returns:
        str: JWT token
    """
    payload = {
        'user_id': user_id,
        'email': email,
        'is_admin': is_admin,
        'exp': datetime.utcnow() + timedelta(hours=JWT_EXP_HOURS),
        'iat': datetime.utcnow()
    }

    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token


def decode_token(token):
    """
    Decode and verify JWT token

    Args:
        token: JWT token string

    Returns:
        dict: Decoded payload
        None: If token is invalid
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def token_required(f):
    """
    Decorator to protect routes that require authentication

    Usage:
        @app.route('/protected')
        @token_required
        def protected_route(current_user):
            return jsonify({'message': f'Hello {current_user["email"]}'})
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Get token from Authorization header
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]  # Format: "Bearer <token>"
            except IndexError:
                return jsonify({'error': 'Invalid token format'}), 401

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        # Verify token
        payload = decode_token(token)
        if not payload:
            return jsonify({'error': 'Token is invalid or expired'}), 401

        # Pass user info to the route
        current_user = {
            'user_id': payload['user_id'],
            'email': payload['email'],
            'is_admin': payload.get('is_admin', False)
        }

        return f(current_user, *args, **kwargs)

    return decorated


def admin_required(f):
    """
    Decorator to protect routes that require admin privileges

    Usage:
        @app.route('/admin')
        @admin_required
        def admin_route(current_user):
            return jsonify({'message': 'Admin access granted'})
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(' ')[1]
            except IndexError:
                return jsonify({'error': 'Invalid token format'}), 401

        if not token:
            return jsonify({'error': 'Token is missing'}), 401

        payload = decode_token(token)
        if not payload:
            return jsonify({'error': 'Token is invalid or expired'}), 401

        if not payload.get('is_admin', False):
            return jsonify({'error': 'Admin access required'}), 403

        current_user = {
            'user_id': payload['user_id'],
            'email': payload['email'],
            'is_admin': payload['is_admin']
        }

        return f(current_user, *args, **kwargs)

    return decorated


def validate_email(email):
    """
    Validate email format

    Args:
        email: Email string

    Returns:
        bool: True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def validate_password(password):
    """
    Validate password strength
    - Minimum 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one number

    Args:
        password: Password string

    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if len(password) < 8:
        return False, 'Password must be at least 8 characters long'

    if not re.search(r'[A-Z]', password):
        return False, 'Password must contain at least one uppercase letter'

    if not re.search(r'[a-z]', password):
        return False, 'Password must contain at least one lowercase letter'

    if not re.search(r'\d', password):
        return False, 'Password must contain at least one number'

    return True, ''


def validate_nif(nif):
    """
    Validate Portuguese NIF (9 digits)

    Args:
        nif: NIF string

    Returns:
        tuple: (bool, str) - (is_valid, error_message)
    """
    if not nif or not nif.isdigit():
        return False, 'NIF must contain only digits'

    if len(nif) != 9:
        return False, 'NIF must have exactly 9 digits'

    # Portuguese NIF validation algorithm
    check_digit = int(nif[8])
    sum_digits = sum(int(nif[i]) * (9 - i) for i in range(8))
    remainder = sum_digits % 11

    if remainder in [0, 1]:
        expected_check = 0
    else:
        expected_check = 11 - remainder

    if check_digit != expected_check:
        return False, 'Invalid NIF check digit'

    return True, ''


def sanitize_input(text):
    """
    Sanitize user input to prevent XSS

    Args:
        text: Input text

    Returns:
        str: Sanitized text
    """
    if not text:
        return text

    # Remove potentially dangerous characters
    dangerous_chars = ['<', '>', '"', "'", '&', ';']
    for char in dangerous_chars:
        text = text.replace(char, '')

    return text.strip()
