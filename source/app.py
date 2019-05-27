from flask import request
from flask import render_template
from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def index():
    gen()
    return render_template('index.html')

def gen():
    os.system("gen.py 0 0 0")
