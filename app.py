from flask import request
from wtforms import Form, BooleanField, StringField, PasswordField, validators
from flask import render_template, url_for, flash
from flask import Flask
from flask import send_from_directory
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename


# coding: utf-8

# In[1]:


from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import pickle
import pandas as pd
import os
import webbrowser
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
import requests
import json



app = Flask(__name__)

UPLOAD_FOLDER = './'

app.secret_key = "secret key"
ALLOWED_EXTENSIONS = set(['csv'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 

@app.route('/')
def index():
	return render_template('index.html')


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	

def gen():
	os.system("bot.sh")
	return render_template('index.html')

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

	



# In[2]:
# Simple Linear Regression

'''
This model predicts the salary of the employ based on experience using simple linear regression model.
'''

# Importing the libraries

# Importing the dataset
dataset = pd.read_csv('out.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values



# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(samples,X, y, test_size = 0.3, random_state = 1/3, train_size = 0.7)
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn import random_projection

import numpy as np

# X is a numpy array of "data" with length 10


#X = ([np.zeros(10)])
#y = ([np.zeros(10)])


#print(len(X_train), len(X_test), len(y_train), len(y_test))


#X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    #train_size=0.7)
#print(len(X_train), len(X_test), len(y_train), len(y_test))

X = dataset["In"].values 
Y = dataset["In"].values
X = format(dataset)

X = np.array([[1]])
np.reshape(X, 1)







model = LinearRegression()  




model.fit(X, y) #training the algorithm
# 3. Check the score
model.score(X, X)



model.intercept_

model.predict(X)


print(str(model.intercept_))

print(X)

f = open('static/outbins.csv', 'w')
f.write(str(X))
f.write("this is our interception:" + str(model.intercept_))
f.write("Our suggestions for use:" + str(model.predict(X)))
f.close()






#put in output: line number/s which causes '1' mark


if __name__ == "__main__":
    app.run(debug=True)

