import pandas as pd
import datetime
import smtplib
from email.message import EmailMessage
import os

def sendEmail(to, sub, msg):
    print(f"email to {to} \nsend with subject: {sub}\n message: {msg}")
    email = EmailMessage()
    email['from'] = 'Sachin Deshmukh'
    email['to'] = f"{to}"
    email['subject'] = f'{sub}'

    email.set_content(f'(msg)')

    with smtlib.SMTP(host ='deshmukhsachin2205@gmail.com', post = 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('Email', 'Password')
        smtp.send_message(email)
        print("Email send")

    pass
if __name__ == "__main__"