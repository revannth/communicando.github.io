#views.py

from app import app

from flask import render_template,url_for

@app.route('/')
@app.route('/literati')
def literati():
	return render_template('index_literati.html')


	
@app.route('/home')
def home():
	return render_template('index.html')


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
@app.route('/.well-known/acme-challenge/X2Pkr_LnjjzoSyRBs21vOhGdJjR_UfnsC0yW7e_20e0')
def ssl():
	return 'X2Pkr_LnjjzoSyRBs21vOhGdJjR_UfnsC0yW7e_20e0.cv6qm5th8axNzQZckSVY86wzXXt95VRO0ZVL2Uy0T1E'