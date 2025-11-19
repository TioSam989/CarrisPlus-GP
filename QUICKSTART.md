# CarrisPlus - Quick Start Guide

## What Has Been Created

A complete authentication system for your CarrisPlus project with:

- **Backend API** (Flask + MySQL) with secure authentication
- **Frontend** (React + Redux) with login and registration
- **Docker** setup so you don't need to install anything on your PC
- **Database** (MySQL) with user and audit tables
- **Security features** (JWT, bcrypt, rate limiting, etc.)

## How to Start (3 Simple Steps)

### Step 1: Make Sure Docker is Running

Open Docker Desktop and make sure it's running.

### Step 2: Start the Application

**Option A - Double-click:**
- Double-click the `START.bat` file in the project folder

**Option B - Command line:**
```bash
cd C:\Users\POP\Documents\CarrisPlus-GP
docker-compose up --build
```

### Step 3: Open Your Browser

After a few minutes (first time takes longer), open:

**http://localhost:3000**

You should see the CarrisPlus login page!

## Using the Application

### Create an Account

1. Click "Registe-se aqui"
2. Fill in the form:
   - Name: Your full name
   - Email: Any valid email
   - NIF: 9 digits (e.g., 123456789)
   - Phone: Optional
   - Password: At least 8 characters, uppercase, lowercase, and numbers
3. Click "Registar"

### Login

1. Enter your email and password
2. Click "Entrar"
3. You'll see the dashboard!

### Logout

Click "Sair" in the top right corner.

## Stopping the Application

**Option A - Double-click:**
- Double-click the `STOP.bat` file

**Option B - Command line:**
- Press `Ctrl+C` in the terminal, then run:
```bash
docker-compose down
```

## What's Running

When you start the application, 3 containers start:

1. **MySQL Database** (port 3306) - Stores user data
2. **Flask Backend** (port 5000) - API for login/register
3. **React Frontend** (port 3000) - The website you see

## Testing API Directly

You can test the API endpoints using tools like Postman or curl:

### Register
```bash
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@test.com\",\"password\":\"Test1234\",\"nif\":\"123456789\",\"full_name\":\"Test User\"}"
```

### Login
```bash
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d "{\"email\":\"test@test.com\",\"password\":\"Test1234\"}"
```

## Files Created

### Backend Files:
```
backend/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker build instructions
├── auth/
│   ├── routes.py           # Login/register endpoints
│   └── utils.py            # JWT tokens, validation
├── models/
│   └── user.py             # User database operations
└── config/
    └── database.py         # MySQL connection
```

### Frontend Files:
```
frontend/
├── src/
│   ├── App.jsx             # Main React app
│   ├── index.js            # Entry point
│   ├── components/
│   │   ├── Auth/
│   │   │   ├── Login.jsx   # Login page
│   │   │   ├── Register.jsx # Register page
│   │   │   └── Auth.css    # Styles
│   │   └── Dashboard.jsx   # Main page after login
│   ├── store/
│   │   ├── store.js        # Redux store
│   │   └── authSlice.js    # Auth state management
│   ├── services/
│   │   ├── api.js          # API client
│   │   └── authService.js  # Auth functions
│   └── utils/
│       └── PrivateRoute.jsx # Protected routes
├── package.json            # Node dependencies
└── Dockerfile             # Docker build instructions
```

### Docker Files:
```
docker-compose.yml          # Orchestrates all services
START.bat                   # Easy start script
STOP.bat                    # Easy stop script
```

## Features Implemented

### Security
- Password hashing with bcrypt
- JWT tokens with 24-hour expiration
- Brute force protection (5 attempts = 15 min lock)
- Portuguese NIF validation
- SQL injection prevention
- XSS/CSRF protection
- Audit logging

### User Management
- User registration with validation
- User login with email/password
- Session management with JWT
- Protected routes
- Automatic token refresh
- Secure logout

### Frontend
- Modern, responsive design
- Form validation
- Error handling
- Loading states
- Redux state management
- Protected routes

## Common Issues

### "Port 3000 is already in use"
Something else is using port 3000. Stop that service or change the port in `docker-compose.yml`.

### "Can't connect to database"
Wait a bit longer. MySQL takes time to initialize on first start (up to 2 minutes).

### "Frontend can't connect to backend"
Make sure all 3 containers are running:
```bash
docker ps
```

You should see:
- carrisplus_db
- carrisplus_backend
- carrisplus_frontend

## Next Steps

Now that authentication works, you can add:

1. **Document Upload** - Let users upload documents
2. **AI Validation** - Validate documents with OCR
3. **Pass Management** - Create and manage passes
4. **Admin Panel** - Manage users and documents
5. **Email Notifications** - Send emails for important events

## Need Help?

1. Check [README_DOCKER.md](README_DOCKER.md) for detailed documentation
2. View logs: `docker logs carrisplus_backend -f`
3. Restart services: `docker-compose restart`
4. Start fresh: `docker-compose down -v && docker-compose up --build`

---

**Everything runs in Docker - nothing installed on your PC!**
