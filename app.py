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

@app.route('/submit-document', methods=['GET', 'POST'])
def submit_document():
    if request.method == 'POST':
        # Handle file upload
        if 'document_file' not in request.files:
            flash('No file selected')
            return redirect(request.url)
        
        file = request.files['document_file']
        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)
        
        if file:
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('Document submitted successfully!')
            return redirect(url_for('index'))
    
    return render_template('submit_document.html')

@app.route('/renew-document')
def renew_document():
    return render_template('renew_document.html')

@app.route('/create-pass')
def create_pass():
    return render_template('create_pass.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)