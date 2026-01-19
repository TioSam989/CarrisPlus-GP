# CarrisPlus - Authentication System Setup

Complete authentication system with Docker for CarrisPlus project.

## Features Implemented

### Backend (Flask + MySQL)
- User registration with validation
- User login with JWT authentication
- Password hashing with bcrypt
- Brute force protection (5 failed attempts = 15 min lock)
- NIF validation (Portuguese tax number)
- Audit logging for all authentication events
- Protected routes with JWT middleware
- CORS configuration for React frontend

### Frontend (React + Redux)
- Login page
- Registration page
- Dashboard (protected route)
- Redux state management
- JWT token storage
- Automatic token refresh
- Form validation
- Error handling
- Responsive design

### Security Features
- HTTPS ready
- JWT tokens with 24h expiration
- Password strength validation
- SQL injection prevention
- XSS protection
- CSRF protection
- Rate limiting
- Account locking after failed attempts

## Prerequisites

- Docker Desktop installed
- Docker Compose installed
- No need to install Python, Node.js, MySQL, or any dependencies!

## Project Structure

```
CarrisPlus-GP/
├── backend/
│   ├── auth/
│   │   ├── routes.py       # Authentication endpoints
│   │   └── utils.py        # JWT and validation utilities
│   ├── models/
│   │   └── user.py         # User model
│   ├── config/
│   │   └── database.py     # Database configuration
│   ├── app.py              # Main Flask application
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Auth/
│   │   │   │   ├── Login.jsx
│   │   │   │   ├── Register.jsx
│   │   │   │   └── Auth.css
│   │   │   ├── Dashboard.jsx
│   │   │   └── Dashboard.css
│   │   ├── store/
│   │   │   ├── authSlice.js
│   │   │   └── store.js
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   └── authService.js
│   │   ├── utils/
│   │   │   └── PrivateRoute.jsx
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── index.js
│   ├── public/
│   │   └── index.html
│   ├── package.json
│   └── Dockerfile
└── docker-compose.yml
```

## Quick Start

### 1. Start All Services

Open a terminal in the project root directory and run:

```bash
docker-compose up --build
```

This will:
- Build and start MySQL database (port 3306)
- Build and start Flask backend API (port 5000)
- Build and start React frontend (port 3000)
- Initialize database tables automatically
- Install all dependencies inside containers

### 2. Wait for Services

Wait for all services to start. You'll see:
- `carrisplus_db` - MySQL ready for connections
- `carrisplus_backend` - Flask running on http://0.0.0.0:5000
- `carrisplus_frontend` - React running on http://localhost:3000

### 3. Access the Application

Open your browser and go to:

**http://localhost:3000**

You should see the login page!

## Testing the Application

### 1. Register a New User

1. Click "Registe-se aqui" on the login page
2. Fill in the registration form:
   - **Nome Completo**: Your full name
   - **Email**: Valid email address
   - **NIF**: 9-digit Portuguese tax number (e.g., 123456789)
   - **Telefone** (optional): Phone number
   - **Password**: At least 8 characters with uppercase, lowercase, and numbers
   - **Confirmar Password**: Same as password

3. Click "Registar"

If successful, you'll be automatically logged in and redirected to the dashboard!

### 2. Login

1. Enter your email and password
2. Click "Entrar"
3. You'll be redirected to the dashboard

### 3. Dashboard

After login, you'll see:
- Welcome message with your name
- Your email and NIF
- Placeholder cards for future features

### 4. Logout

Click "Sair" button in the header to logout.

## API Endpoints

### Authentication

#### Register User
```http
POST http://localhost:5000/api/auth/register
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "SecurePass123",
    "nif": "123456789",
    "full_name": "John Doe",
    "phone": "+351912345678"
}
```

#### Login User
```http
POST http://localhost:5000/api/auth/login
Content-Type: application/json

{
    "email": "user@example.com",
    "password": "SecurePass123"
}
```

#### Get Current User
```http
GET http://localhost:5000/api/auth/me
Authorization: Bearer <your_jwt_token>
```

#### Logout
```http
POST http://localhost:5000/api/auth/logout
Authorization: Bearer <your_jwt_token>
```

## Database Schema

### users Table
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- email (VARCHAR 255, UNIQUE, NOT NULL)
- password_hash (VARCHAR 255, NOT NULL)
- nif (VARCHAR 9, UNIQUE, NOT NULL)
- full_name (VARCHAR 255, NOT NULL)
- phone (VARCHAR 20, NULL)
- created_at (TIMESTAMP)
- updated_at (TIMESTAMP)
- is_active (BOOLEAN, DEFAULT TRUE)
- is_admin (BOOLEAN, DEFAULT FALSE)
- failed_login_attempts (INT, DEFAULT 0)
- locked_until (TIMESTAMP, NULL)
```

### audit_logs Table
```sql
- id (INT, PRIMARY KEY, AUTO_INCREMENT)
- user_id (INT, FOREIGN KEY)
- action (VARCHAR 100, NOT NULL)
- entity_type (VARCHAR 50)
- entity_id (INT)
- ip_address (VARCHAR 45)
- user_agent (TEXT)
- details (JSON)
- created_at (TIMESTAMP)
```

## Stopping the Services

To stop all services:

```bash
docker-compose down
```

To stop and remove all data (including database):

```bash
docker-compose down -v
```

## Troubleshooting

### Port Already in Use

If ports 3000, 5000, or 3306 are already in use:

1. Stop the conflicting service, OR
2. Edit `docker-compose.yml` and change the port mappings:

```yaml
ports:
  - "3001:3000"  # Frontend
  - "5001:5000"  # Backend
  - "3307:3306"  # MySQL
```

### Database Connection Issues

If backend can't connect to database:

1. Wait a bit longer (MySQL takes time to initialize)
2. Check if database container is healthy:
   ```bash
   docker ps
   ```
3. Restart services:
   ```bash
   docker-compose restart
   ```

### Frontend Can't Connect to Backend

1. Make sure backend is running:
   ```bash
   docker logs carrisplus_backend
   ```

2. Check if you can access the API directly:
   - Open http://localhost:5000 in your browser
   - You should see the API info

### Clear Everything and Start Fresh

```bash
docker-compose down -v
docker-compose up --build
```

## Accessing Database Directly

To access MySQL database:

```bash
docker exec -it carrisplus_db mysql -u carrisplus_user -p
```

Password: `carrisplus_pass`

Then:
```sql
USE carrisplus;
SHOW TABLES;
SELECT * FROM users;
SELECT * FROM audit_logs;
```

## Viewing Logs

### Backend Logs
```bash
docker logs carrisplus_backend -f
```

### Frontend Logs
```bash
docker logs carrisplus_frontend -f
```

### Database Logs
```bash
docker logs carrisplus_db -f
```

## Development

### Making Changes

**Backend**: Changes to Python files will auto-reload (Flask debug mode).

**Frontend**: Changes to React files will trigger hot reload.

### Adding New Dependencies

**Backend**:
1. Add package to `backend/requirements.txt`
2. Rebuild: `docker-compose up --build backend`

**Frontend**:
1. Add package to `frontend/package.json`
2. Rebuild: `docker-compose up --build frontend`

## Security Notes

**IMPORTANT**: Before deploying to production:

1. Change `JWT_SECRET_KEY` in `docker-compose.yml`
2. Change `MYSQL_ROOT_PASSWORD` and `MYSQL_PASSWORD`
3. Use environment variables file (`.env`)
4. Enable HTTPS
5. Set `FLASK_ENV=production`
6. Review CORS settings

## Next Steps

Now that authentication is working, you can:

1. Implement document upload functionality
2. Add pass management features
3. Create admin panel
4. Add email notifications
5. Implement OCR validation

## Support

If you encounter any issues:

1. Check the logs (commands above)
2. Verify all containers are running: `docker ps`
3. Make sure ports are not in use
4. Try rebuilding: `docker-compose up --build`

---

**Created for CarrisPlus - Desenvolvimento de Software B**
