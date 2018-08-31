from flask import render_template, url_for, redirect, request
from flask_dance.contrib.google import google
from flask_login import current_user, login_user
from app import app, db, login
from models import User, Roles


@app.route("/")
def home():
	if not google.authorized:
		return redirect(url_for("google.login"))
	resp = google.get("/oauth2/v2/userinfo")
	emailUser = resp.json()["email"]
	print(emailUser)
	print(request.headers)
	if emailUser == "support@ebizontek.com":
		user = User.query.filter_by(email=emailUser).first()
		if user is None:
			user = User(email=emailUser)
			role = Roles(user_id=user.id, role="Admin")
			db.session.add(user)
			db.session.add(role)
			db.session.commit()
			login_user(user)
			return redirect(url_for("admin"))
		else:		
			login_user(user)
			return redirect(url_for("admin"))
	else:
		user = User.query.filter_by(email=emailUser).first()
		if user is None:
			return "You are not allowed to do staging"
		else:
			login_user(user)
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
	if not current_user.is_authenticated:
		return redirect(url_for("google.login"))
	return render_template("registration.html")

@app.route("/add/user", methods=["POST"])
def addUser():
	if not current_user.is_authenticated:
		email = request.form["email"]
		if email.strip():
			userEmail = email+"@ebizontek.com"
			user = User(email=userEmail)
			db.session.add(user)
     		db.session.commit()
     		return "You Have Added A User"


@login.user_loader
def load_user(id):
    return User.query.get(int(id))     		

