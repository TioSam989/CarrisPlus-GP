# CarrisPlus - Document Management System

A Flask-based web application for online document submission, renewals, and pass creation.

## Features
- Online document submission
- Document renewal requests
- Pass/permit creation
- User-friendly interface

## Technologies
- Python 3.11
- Flask
- HTML/CSS/JavaScript
- Jinja2 templating
- Docker

## Quick Start with Docker

### Prerequisites
- Docker Desktop installed on Windows 11
- Git (optional, for version control)

### Running the Application

1. **Clone or download the project**
2. **Open Command Prompt or PowerShell in the project directory**
3. **Build and run with Docker Compose:**
   ```bash
   docker-compose up --build
   ```
4. **Access the application at:** http://localhost:5000

### Development Mode
The Docker setup includes volume mounting, so code changes will be reflected immediately without rebuilding.

### Stopping the Application
```bash
docker-compose down
```

## Project Structure
```
CarrisPlus-GP/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose setup
├── templates/         # HTML templates
├── static/           # CSS, JS, images
└── uploads/          # Document uploads
```

## Team Development
Each team member can:
1. Clone the repository
2. Run `docker-compose up --build`
3. Start developing immediately

No need to install Python, Flask, or manage virtual environments - Docker handles everything!