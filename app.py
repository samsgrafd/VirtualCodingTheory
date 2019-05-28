from flask import request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import render_template, url_for, flash
from flask import Flask
from flask import send_from_directory
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

UPLOAD_FOLDER = './'

app.secret_key = "secret key"
ALLOWED_EXTENSIONS = set(['txt'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 

def gen():
	os.system("/home/site/wwwroot/bot.bat")

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	gen()
	return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File(s) successfully uploaded')
			return redirect('/')

   
@app.route('/', methods=['GET','POST'])
def index():
	
	
	return render_template('index.html')



 
if __name__ == "__main__":
    app.run()