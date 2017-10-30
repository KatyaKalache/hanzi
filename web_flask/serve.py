#!/usr/bin/python3
# starts a Flask web application
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def decomp():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
