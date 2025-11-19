"""
CarrisPlus Backend API
Main Flask application with authentication
"""
from flask import Flask, jsonify
from flask_cors import CORS
from auth.routes import auth_bp
from config.database import init_database
import os
import time

app = Flask(__name__)

# CORS configuration - Allow React frontend
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:3000",
            "http://frontend:3000",
            "https://carris-plus-gp.vercel.app",
            "https://carris-plus-gp-tiosam989.vercel.app",
            "https://*.vercel.app",
            "https://*.onrender.com"
        ],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "expose_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

# Configuration
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'your-super-secret-jwt-key-change-in-production')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Register blueprints
app.register_blueprint(auth_bp)


@app.before_request
def before_first_request():
    """Initialize database on first request"""
    if not hasattr(app, 'db_initialized'):
        max_retries = 10
        retry_count = 0

        while retry_count < max_retries:
            try:
                print(f"Attempting to initialize database (attempt {retry_count + 1}/{max_retries})...")
                init_database()
                app.db_initialized = True
                print("Database initialized successfully!")
                break
            except Exception as e:
                retry_count += 1
                print(f"Failed to initialize database: {e}")
                if retry_count < max_retries:
                    print(f"Retrying in 3 seconds...")
                    time.sleep(3)
                else:
                    print("Max retries reached. Database initialization failed.")
                    raise


@app.route('/')
def index():
    """API root endpoint"""
    return jsonify({
        'message': 'CarrisPlus API',
        'version': '1.0.0',
        'endpoints': {
            'auth': {
                'register': 'POST /api/auth/register',
                'login': 'POST /api/auth/login',
                'me': 'GET /api/auth/me',
                'logout': 'POST /api/auth/logout'
            }
        }
    })


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'CarrisPlus Backend API'
    })


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
