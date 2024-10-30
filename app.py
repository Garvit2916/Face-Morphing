from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Define the folder to store uploaded files (if you're using file uploads)
UPLOAD_FOLDER = 'uploads/'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    # Render the HTML page for the face-swapping feature
    return render_template('Massey_Ferguson_Face_Swapping_Feature.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload from the HTML form
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)
