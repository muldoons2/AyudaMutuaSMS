import os
import requests
from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from twilio.rest import Client

app = Flask(__name__)
app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))

### List of phone numbers, comma separated. You can add more numbers to this list. 
# SBM_nums = ['+19144699732','+19142827342']

### Same basic function as before, but "to" is now a variable called x
def send_sms(from_num,to_num,sid,token,body_text):
    account_sid = sid
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=body_text,
                         from_=from_num,
                         to= to_num
                     )

# ### This is a "loop" that repeats the function for each number on the list. 
# for y in nums:
#     send_sms(SBM_num)

twil_list=[]

###################################################
@app.route('/')
def index():
    return render_template('home.html')

###################################################
@app.route("/register", methods=["POST"])
def register():
    from_num = request.form.get("from_num")
    to_num = request.form.get("to_num")
    sid = request.form.get("sid")
    token = request.form.get("token")
    body_text = request.form.get("body_text")
#     x = [from_num,to_num,sid,token, body]
#     twil_list.append(x)
    twil_list.append(from_num)
    twil_list.append(to_num)
    twil_list.append(sid)
    twil_list.append(token)
    twil_list.append(body_text)
    send_sms(from_num,to_num,sid,token,body_text)
    
    return redirect('/twilio')

###################################################
@app.route("/twilio")
def twilio():
    return render_template('twilio.html',twil_list=twil_list)

###################################################
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
