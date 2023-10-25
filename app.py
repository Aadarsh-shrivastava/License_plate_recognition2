import os
from flask import Flask, request, render_template
from base import get_license_plate_data as glpd

app = Flask(__name__)

# Define the upload folder
if not os.path.exists('uploads'):
    os.mkdir('uploads')
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to check if the uploaded file is allowed
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        data=glpd(filename)
       
        print(data)
        
        return render_template("result.html",data=data)

    return "Invalid file format"

if __name__ == '__main__':
    app.run(debug=True)
