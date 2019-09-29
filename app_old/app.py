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
import vcode as vc


app = Flask(__name__)

UPLOAD_FOLDER = './'

app.secret_key = "secret key"
ALLOWED_EXTENSIONS = set(['txt'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 

f = ""

def gen():
	os.system("bot.sh")

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

	@app.route('/', methods=['GET','POST'])
	def my_form_post():
		text = request.form['text']
		processed_text = text.upper()
		return processed_text
	f = text
	def my_form():
    		return render_template('index.html')
	
	
	return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def my_form_post2():
	
	my_form2()
def my_form2():
    return webbrowser.open_new_tab('predict.txt')


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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/6, random_state = 1/3)

# Fitting Simple Linear Regression to the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predicting the Test set results
y_pred = regressor.predict(X_test)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load( open('model.pkl','rb'))
print(model.predict([[1.8]]))


# Get headers for payload
headers = ['11', '01', '011', '01', '10', '00', '1', '010']


# In[3]:
f = { "lion": "yellow", "kitty": "red" }
for key, value in f.items():
	print(key, value)

#tee downloadable file button ja yhdistä se metodiin tänne   
pickle.dump( f, open( "binary.pkl", "wb" ) )

model = pickle.load( open( "binary.pkl", "rb" ) )

# In[4]:


# Test model with data frame
input_variables = pd.DataFrame([[1, 106, 70, 28, 135, 34.2, 0.142, 22]],
                                columns=headers, 
                                dtype=float,
                                index=['input'])

# Get the model's prediction
prediction = model.predict(input_variables)
print("Prediction: ", prediction)
prediction_proba = model.predict_proba(input_variables)
print("Probabilities: ", prediction_proba)
f = open("predict.txt", 'w')
f.write(str(prediction) + str(prediction_proba))
f.close()

# In[ ]:



@app.route("/katana-ml/api/v1.0/diabetes", methods=['POST'])
def predict():
    payload = request.json['data']
    values = [float(i) for i in payload.split(',')]
    
    input_variables = pd.DataFrame([values],
                                columns=headers, 
                                dtype=float,
                                index=['input'])

    # Get the model's prediction
    prediction_proba = model.predict_proba(input_variables)
    prediction = (prediction_proba[0])[1]
    
    ret = '{"prediction":' + str(float(prediction)) + '}'
    
    return ret

# running REST interface, port=5000 for direct test

Inall=""
Inb="01"
current=""
binaryCount=0
str1 =""
dslArray1 =[]
dslArray2 =[]
output= "output.txt"
propability= 0
binaryCount= 0
serach= ""
count= 0
f = open("static/outbins.txt", 'r')

Inall = f.read()

f.close()

print("this is inputStrBin:" + Inall)	


if Inb in Inall:
                        
        Inb="0"
        print("this is Inall + Inb:" + Inall + Inb)	

if Inb in Inall:
        for i in Inall:

                binaryCount += 1

                current += i

                binaryCount +=1

                if(binaryCount > 0 and current =="0"):

		

                    dslArray1 +="1"

                    dslArray2 += "0"

                    dslArray1 += Inall
	    
                
                        

for i, s in enumerate(dslArray1):

	  			s +="1"
	  			dslArray1[i] = s.strip()

str1 = ''.join(dslArray1)

propability = propability/binaryCount

dslArray1 +=("1",propability,propability, binaryCount)

f = open(output, 'w')

f.write(str1 + str(dslArray1) + str(dslArray2))

f.close()

print(binaryCount)

print(propability)

print(str(dslArray1))

print(str(dslArray2))

print(Inall)

#put in output: line number/s which causes '1' mark


if __name__ == "__main__":
    app.run(debug=True)

