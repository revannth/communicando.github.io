#views.py

from app import app

from flask import render_template,url_for

@app.route('/register')
def register():
	return render_template('register.html')

	



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