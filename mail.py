#mail.py
from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail,  Message

app = Flask(__name__)

@app.route('/send-mail/')
def send_mail():
    msg = mail.send_message(
        'Send Mail tutorial!',
        sender='revannth1997@gmail.com',
        recipients=['revannth1997@gmail.com'],
        body="Congratulations you've succeeded!"
    )
    return 'Mail sent'

if __name__ == '__main__':
	app.run(debug=True)
