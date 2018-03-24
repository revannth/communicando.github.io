#mail.py
from flask import Flask, render_template, redirect, url_for
from flask_mail import Mail,  Message

app = Flask(__name__)
app.config.update(
    MAIL_SERVER='smtp.googlemail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME = 'revannth1997@gmail.com',
    MAIL_PASSWORD = 'r3va99th1nn7'
)

mail = Mail(app)

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