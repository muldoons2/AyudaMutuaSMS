import os
import requests
from flask import Flask, render_template, url_for
from datetime import datetime
app = Flask(__name__)

@app.route("/")
def home(): return render_template('home.html')

# @app.route("/submit")
# def submit():
#     ye_quote= requests.get("https://api.kanye.rest").json()['quote']
#     return render_template('kanye.html',value=ye_quote)

############### #Twilio API

# # Download the helper library from https://www.twilio.com/docs/python/install
# from twilio.rest import Client


# # Your Account Sid and Auth Token from twilio.com/console
# # DANGER! This is insecure. See http://twil.io/secure
# account_sid = 'AC0f09286ecbe74943e0513a4fa26a8310'
# auth_token = '8fb298894527a2c7673fdab7e39754ec'
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Test Text. Built by Sean Muldoon on the Twilio API",
#                      from_='+19175254826',
#                      to='+19144699732'
#                  )

# print(message.sid)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)