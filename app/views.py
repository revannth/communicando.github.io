#views.py

from app import app,mail,db
from flask import render_template,url_for,redirect,request,flash
from threading import Thread
from flask_mail import Message
from . models import Participant

def send_asyncemail(app,msg):
	with app.app_context():
		mail.send(msg)


@app.route('/register')
def register():
	return render_template('register.html')

	

@app.route('/send_email',methods=['POST'])
def send_email():

	#Database entry

	name = request.form['Name']
	email = request.form['Email']
	college = request.form['College']
	mobile = request.form['Mobile']
	event = request.form['Event']

	partipant_add = Participant(name=name,email=email,college=college,mobile=mobile,event=event)
	db.session.add(partipant_add)
	db.session.commit()



	msg = Message("Literati 8.0 Welcomes you {}".format(name),sender="revannth1997@gmail.com",recipients=[email])
	msg.body="Thank you for registring for Literati 8.0"
	msg.html='''<h1> CBIT Communicando Welcomes You</h1>
				<img src="https://cdn.discordapp.com/attachments/396209702528090115/411968753602134019/unknown.png"></img>
				You have signed up for {}!
				Follow our Facebook page or keep an eye on the website for further updates'''.format(event)
	Thread(target=send_asyncemail,args=(app,msg)).start()
	return render_template('confirmation.html')
	



#Just Views

@app.route('/error')
def error():
	return render_template('404.html')

#Main Landing Page(Switched during Literati)
@app.route('/home')
def home():
	return render_template('index.html')

#Literati Handle
@app.route('/')
@app.route('/literati')
def literati():
	return render_template('index_literati.html')


@app.route('/about')
def about():
	return render_template('about.html')
@app.route('/landing')
def landing():
	return render_template('index_landing.html')
@app.route('/juniorcoord')
def ourteam():
	return render_template('Our_team1.html')
@app.route('/seniorcoords')
def ourteamsen():
	return render_template('Our_team2.html')




## SSL
@app.route('/.well-known/acme-challenge/F-8p_89nhmwhcw0esSKdOGoxLWx53vtZduj9XSaT_b4')
def ssl():
	return 'F-8p_89nhmwhcw0esSKdOGoxLWx53vtZduj9XSaT_b4.cv6qm5th8axNzQZckSVY86wzXXt95VRO0ZVL2Uy0T1E'