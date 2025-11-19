"""
Database configuration and connection management
"""
import pymysql
import os
from contextlib import contextmanager

# Database configuration from environment variables
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'db'),
    'user': os.getenv('DB_USER', 'carrisplus_user'),
    'password': os.getenv('DB_PASSWORD', 'carrisplus_pass'),
    'database': os.getenv('DB_NAME', 'carrisplus'),
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}


def get_db_connection():
    """
    Create and return a database connection
    """
    try:
        connection = pymysql.connect(**DB_CONFIG)
        return connection
    except pymysql.Error as e:
        print(f"Error connecting to database: {e}")
        raise


@contextmanager
def get_db_cursor(commit=False):
    """
    Context manager for database operations

    Args:
        commit: Whether to commit the transaction

    Usage:
        with get_db_cursor(commit=True) as cursor:
            cursor.execute("INSERT INTO users ...")
    """
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        yield cursor
        if commit:
            connection.commit()
    except Exception as e:
        connection.rollback()
        raise e
    finally:
        cursor.close()
        connection.close()


def init_database():
    """
    Initialize database tables
    """
    with get_db_cursor(commit=True) as cursor:
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password_hash VARCHAR(255) NOT NULL,
                nif VARCHAR(9) UNIQUE NOT NULL,
                full_name VARCHAR(255) NOT NULL,
                phone VARCHAR(20),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT TRUE,
                is_admin BOOLEAN DEFAULT FALSE,
                failed_login_attempts INT DEFAULT 0,
                locked_until TIMESTAMP NULL,
                INDEX idx_email (email),
                INDEX idx_nif (nif)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        ''')

        # Audit logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_logs (
                id INT AUTO_INCREMENT PRIMARY KEY,
                user_id INT,
                action VARCHAR(100) NOT NULL,
                entity_type VARCHAR(50),
                entity_id INT,
                ip_address VARCHAR(45),
                user_agent TEXT,
                details JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
                INDEX idx_user_id (user_id),
                INDEX idx_action (action),
                INDEX idx_created_at (created_at)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        ''')

        print("Database tables initialized successfully!")
