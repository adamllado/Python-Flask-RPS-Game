from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
import random
from flask import request
    
class PlayAgain(FlaskForm):
    submit = SubmitField('Play Again?')
    