from flask import Flask, render_template, url_for, request
from reseau import *

app = Flask(__name__)

@app.route("/")
@app.route("/accueil")
def index():
    return render_template('accueil.html')
      
@app.route("/reseau", methods=['GET', 'POST'])
def reseau():
	ip, masque, ipdebut, ipfin = LireIpStatique()
	if request.method == 'POST':
		if request.form['IPstatique']and request.form['MASQUEstatique']:
			IPstatique = request.form['IPstatique']
			MASQUEstatique = request.form['MASQUEstatique']
			ChangerIPstatique(IPstatique, MASQUEstatique)
			ip, masque, ipdebut, ipfin = LireIpStatique()
		else:
			return "unvalide"
	return render_template('reseau.html', ip=ip, masque=masque)
    #https://openclassrooms.com/fr/courses/1654786-creez-vos-applications-web-avec-flask/1655474-lechange-de-donnees
    
@app.route("/serveur")
def serveur():
    return render_template('serveur.html')
    
@app.route("/support")
def support():
    return render_template('support.html')

if __name__ == "__main__":
    app.run()

