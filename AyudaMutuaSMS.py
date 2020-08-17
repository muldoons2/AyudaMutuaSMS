import os
import requests
from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home(): return render_template('home.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        recipient = request.form['recipient']
        return render_template('submit.html',recipient=recipient)
    return render_template('submit.html')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
