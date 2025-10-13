from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-change-this'
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit-document')
def submit_document():
    return render_template('submit_document.html')

@app.route('/renew-document')
def renew_document():
    return render_template('renew_document.html')

@app.route('/create-pass')
def create_pass():
    return render_template('create_pass.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)