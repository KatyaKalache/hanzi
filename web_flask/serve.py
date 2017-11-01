#!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template, request
from dev import test
from pymongo import MongoClient
import re

decom = test.decom
app = Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET'])
def display():
    return render_template('text.html')

@app.route('/hello', methods=['GET', 'POST'], strict_slashes=False)
def char():
    argument = request.form['first_name']
    word_associations = decom(argument)
    return word_associations

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
