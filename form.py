from flask import request
from flask import render_template
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
import os

class ContactForm(FlaskForm):

    submit = SubmitField('Do this')
    submit2 = SubmitField('Do that')