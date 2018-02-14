#views.py

from app import app,mail,db
from flask import render_template,url_for,redirect,request,flash
from threading import Thread
from flask_mail import Message
from . models import Participant
import random


links = {'Human Library':'https://cdn.discordapp.com/attachments/412220459002888203/412221165831192579/Human_Library_poster.png','Write Angle':'https://cdn.discordapp.com/attachments/412220459002888203/412221167009529871/2018-02-09-PHOTO-00272147.jpg','CrossFire':'https://cdn.discordapp.com/attachments/412220459002888203/412221174739894272/finalcross.jpg','Kahanikaar':'https://cdn.discordapp.com/attachments/412220459002888203/412221174756671489/kahaani_final_with_lanscape_mode-1.jpg','Matlaata':'https://cdn.discordapp.com/attachments/412220459002888203/412221174999941120/maatlalata_land.jpg','Mr. and Ms. Literati':'https://cdn.discordapp.com/attachments/412220459002888203/412221176082071552/Anukrutis.jpg','Informals':'https://cdn.discordapp.com/attachments/412220459002888203/412221176417615883/Informal_Poster_Final.jpg','Whodunnit':'https://cdn.discordapp.com/attachments/412220459002888203/412221189587730443/IMG-20180210-WA0004.jpg','A Good Day to Quiz Hard':'https://cdn.discordapp.com/attachments/412220459002888203/412223889180065792/Literati1-page-001.jpg'}
nums = {'Mr. and Ms. Literati':2,'CrossFire':3,'Whodunnit':4,'A Good Day to Quiz Hard':5,'Kahanikaar':6,'Matlaata':7,'Human Library':8,'Write Angle':9,'Informals':1,'Open Mic':11}
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
	hear = request.form['Hear']
	experience = request.form['Experience']
	regnum = str(nums[event])+'00'+str(random.randint(0,100000)) 
	partipant_add = Participant(name=name,email=email,college=college,mobile=mobile,event=event,regnum=regnum,hear=hear,experience=experience)
	db.session.add(partipant_add)
	db.session.commit()
	link = links[event]


	msg = Message("Literati 8.0 Welcomes you {}".format(name),sender="revannth1997@gmail.com",recipients=[email])
	msg.body="Thank you for registring for Literati 8.0"
	msg.html= render_template('hero.html',name=name,event=event,link=link,regnum=regnum)
	Thread(target=send_asyncemail,args=(app,msg)).start()
	return render_template('confirmation.html')
	

#Email view for verifying outlook of the Mail template
'''@app.route('/email')
def email():
	return render_template('hero.html')'''
#Just Views

@app.route('/error')
def error():
	return render_template('404.html')

#Main Landing Page(Switched during Literati)
@app.route('/home')
def home():
	return render_template('index.html')

@app.route('/juniorcoord')
def juniorcoord():
	return render_template('Our_team1.html')
@app.route('/seniorcoords')
def seniorcoords():
	return render_template('Our_team2.html')

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





## SSL
@app.route('/.well-known/acme-challenge/F-8p_89nhmwhcw0esSKdOGoxLWx53vtZduj9XSaT_b4')
def ssl():
	return 'F-8p_89nhmwhcw0esSKdOGoxLWx53vtZduj9XSaT_b4.cv6qm5th8axNzQZckSVY86wzXXt95VRO0ZVL2Uy0T1E'