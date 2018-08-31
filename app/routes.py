from flask import render_template, url_for, redirect, request
from flask_dance.contrib.google import google
from app import app, db
from models import User


@app.route("/")
def home():
	if not google.authorized:
		return redirect(url_for("google.login"))
	resp = google.get("/oauth2/v2/userinfo")
	emailUser = resp.json()["email"]
	if emailUser == "support@ebizontek.com":
		return redirect(url_for("admin"))
	else:
		user = User.query.filter_by(email=emailUser).first()
		if user is None:
			return "You are not allowed to do staging"
		else:
			return redirect(url_for("instance"))	
			

@app.route("/admin")
def admin():
	if not google.authorized:
		return redirect(url_for("google.login"))
	resp = google.get("/oauth2/v2/userinfo")
	emailUser = resp.json()["email"]
	if emailUser == "support@ebizontek.com":
		users = User.query.all()
		return render_template("admin.html", users=users)
	else:
		return "You are not authorized to access here"	

@app.route("/instance")
def instance():
	if not google.authorized:
		return redirect(url_for("google.login"))
	return render_template("registration.html")

@app.route("/add/user", methods=["POST"])
def addUser():
	if google.authorized:
		email = request.form["email"]
		if email.strip():
			userEmail = email+"@ebizontek.com"
			user = User(email=userEmail)
			db.session.add(user)
     		db.session.commit()
     		return "You Have Added A User"

