import pandas as pd
from flask import request, redirect, Flask

app = Flask(__name__)


# Overview:
# Simple app to verify email and password
# We get the email and password via web and validate from csv file

@app.route('/')
def welcome_msg():
    """
    When the user is authenticated
    :return: "Welcome page"
    """
    return "Welcome"


@app.route('/wrongemail')
def wrong_email():
    """
    In case there is no such email present
    :return: Error msg
    """
    return "Wrong Email. Please check and re-enter"


@app.route('/wrongpass')
def wrong_password():
    """
    In case the email exists, but the password is incorrect
    :return: Error text
    """
    return "Wrong Password."


@app.route('/signup', methods=['POST'])
def signup():
    """
    API to call from the front end which validates the email and password
    :return:
    """
    print('here')
    email = request.form['email']
    password = request.form['password']
    df = pd.read_csv('validation_emails.csv')
    if str(email).lower() not in list(df['email'].unique()):
        return redirect('/wrongemail')
    else:
        orig_pass = df.loc[df['email'] == email].copy()['password'].values[0]
        if password != orig_pass:
            return redirect('/wrongpass')
        else:
            return redirect('/')
