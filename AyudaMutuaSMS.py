import os
import requests
from flask import Flask, render_template, url_for, redirect, request
from twilio.rest import Client
app = Flask(__name__)
app.config.update(dict(SECRET_KEY="powerful secretkey", WTF_CSRF_SECRET_KEY="a csrf secret key"))

###################################################
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
