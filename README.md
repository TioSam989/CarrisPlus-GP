# CarrisPlus - Document Management System

> **Solving Documentation Challenges Through Digital Innovation**

A modern Flask-based web application designed to eliminate unnecessary travel and waiting times for document processing. CarrisPlus enables citizens to submit documents, request renewals, and create passes entirely online.

## 🎯 Problem Statement

**Current Issues:**
- Difficulty handling documentation requiring physical presence
- Unnecessary travel for simple document submissions
- Long waiting times for basic administrative tasks
- Challenges for people with time constraints and mobility issues

**Our Solution:**
A comprehensive online platform that digitizes the entire document submission process, making government services accessible from anywhere, anytime.

## ✨ Features

- 📄 **Online Document Submission** - Upload and submit documents digitally
- 🔄 **Document Renewal Requests** - Renew existing documents without visiting offices
- 🎫 **Pass/Permit Creation** - Generate new passes and permits online
- 👥 **User-Friendly Interface** - Intuitive design for all age groups
- 🔒 **Secure File Handling** - Safe document upload and storage
- 📱 **Responsive Design** - Works on desktop, tablet, and mobile

## 🛠️ Technologies

- **Backend:** Python 3.11, Flask
- **Frontend:** HTML5, CSS3, JavaScript
- **Templating:** Jinja2
- **Containerization:** Docker & Docker Compose
- **Version Control:** Git

### Required Software
- Docker Desktop (includes Docker Compose)
- Git (optional, for cloning repository)
- Web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Complete Setup Guide

### Step 1: Install Docker Desktop

#### Windows 11/10:
1. Download Docker Desktop from: https://www.docker.com/products/docker-desktop/
2. Run the installer as Administrator
3. Follow installation wizard (enable WSL 2 if prompted)
4. Restart your computer
5. Launch Docker Desktop and wait for it to start
6. Verify installation:
   ```bash
   docker --version
   docker-compose --version
   ```

#### Linux (Ubuntu/Debian):
```bash
# Update package index
sudo apt update

# Install Docker
sudo apt install docker.io docker-compose

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker

# Add user to docker group
sudo usermod -aG docker $USER

# Logout and login again
```

### Step 2: Get the Project

#### Option A: Clone with Git
```bash
git clone https://github.com/your-username/CarrisPlus-GP.git
cd CarrisPlus-GP
```

#### Option B: Download ZIP
1. Download project ZIP file
2. Extract to desired location
3. Open terminal in project folder

### Step 3: Run the Application

#### First Time Setup:
```bash
# Navigate to project directory
cd CarrisPlus-GP

# Build and start containers
docker-compose up --build

# Wait for "Running on http://0.0.0.0:5000" message
```

#### Subsequent Runs:
```bash
# Start existing containers
docker-compose up

# Or run in background
docker-compose up -d
```

### Step 4: Access the Application

1. Open your web browser
2. Navigate to: **http://localhost:5000**
3. You should see the CarrisPlus homepage

## 🔧 Development Commands

```bash
# View running containers
docker ps

# View application logs
docker-compose logs web

# Stop the application
docker-compose down

# Rebuild after code changes
docker-compose up --build

# Enter container for debugging
docker exec -it carrisplus-gp-web-1 bash

# Install additional Python packages
docker exec -it carrisplus-gp-web-1 pip install package-name
```

## 📁 Project Structure

```
CarrisPlus-GP/
├── 📄 app.py                 # Main Flask application
├── 📄 requirements.txt       # Python dependencies
├── 🐳 Dockerfile            # Container configuration
├── 🐳 docker-compose.yml    # Multi-container setup
├── 📄 .dockerignore         # Docker build exclusions
├── 📁 templates/            # HTML templates
│   ├── base.html           # Base template
│   └── index.html          # Homepage
├── 📁 static/              # Static assets
│   ├── css/               # Stylesheets
│   └── js/                # JavaScript files
└── 📁 uploads/             # Document storage
```

## 👥 Team Development Workflow

### For Each Team Member:

1. **Initial Setup:**
   ```bash
   git clone <repository-url>
   cd CarrisPlus-GP
   docker-compose up --build
   ```

2. **Daily Development:**
   ```bash
   git pull origin main
   docker-compose up
   # Make your changes
   git add .
   git commit -m "Your changes"
   git push origin your-branch
   ```

3. **Adding New Dependencies:**
   ```bash
   # Add to requirements.txt
   echo "new-package==1.0.0" >> requirements.txt
   
   # Rebuild container
   docker-compose up --build
   ```

## 🐛 Troubleshooting

### Common Issues:

**Docker not starting:**
- Ensure Docker Desktop is running
- Check system tray for Docker whale icon
- Restart Docker Desktop if needed

**Port 5000 already in use:**
```bash
# Kill process using port 5000
sudo lsof -ti:5000 | xargs kill -9

# Or change port in docker-compose.yml
ports:
  - "8000:5000"  # Use port 8000 instead
```

**Permission errors on Windows:**
- Run terminal as Administrator
- Or use WSL2 terminal instead

**Container build fails:**
```bash
# Clean Docker cache
docker system prune -a

# Rebuild from scratch
docker-compose build --no-cache
```

## 🚀 Next Steps

1. **Expand Features:**
   - Add user authentication
   - Implement file upload validation
   - Create admin dashboard
   - Add email notifications

2. **Database Integration:**
   - Uncomment database service in docker-compose.yml
   - Add SQLAlchemy models
   - Implement data persistence

3. **Production Deployment:**
   - Configure environment variables
   - Set up reverse proxy (Nginx)
   - Implement SSL certificates
   - Add monitoring and logging

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Docker Desktop documentation
3. Contact team members for assistance

---

**Built with ❤️ for better citizen services**