import os
import requests
from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home(): return render_template('home.html')

@app.route("/sample_form")
def sample_form(): return render_template('sample_form.html')

@app.route('/submit')
def submit():
    fname = request.form['fname']
    return render_template('submit.html',fname=fname)



if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
