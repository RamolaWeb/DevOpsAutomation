from flask import render_template, url_for, redirect, request, jsonify
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
	if emailUser == "sahil.ramola@ebizontek.com":
		user = User.query.filter_by(email=emailUser).first()
		if user is None:
			user = User(email=emailUser)
			db.session.add(user)
			db.session.flush()
			role = Roles(user_id=user.id, role="Admin")
			db.session.add(role)
			db.session.commit()
			login_user(user, remember=True)
			return redirect(url_for("admin"))
		else:		
			login_user(user)
			return redirect(url_for("admin"))
	else:
		user = User.query.filter_by(email=emailUser).first()
		if user is None:
			return "You are not allowed to do staging"
		else:
			login_user(user, remember=True)
			return redirect(url_for("instance"))	
			

@app.route("/admin")
def admin():
	if not current_user.is_authenticated:
		return redirect(url_for("google.login", referer="admin"))
	resp = google.get("/oauth2/v2/userinfo")
	emailUser = resp.json()["email"]
	if emailUser == "sahil.ramola@ebizontek.com":
		users = User.query.all()
		return render_template("admin.html", users=users)
	else:
		return "You are not authorized to access here"	

@app.route("/instance")
def instance():
	if not current_user.is_authenticated:
		return redirect(url_for("google.login", referer="instance"))
	roleUser = Roles.query.filter_by(user_id=current_user.id).first()
	if roleUser is not None:
		if roleUser.role == "Admin" or roleUser.role == "Lead":
			return render_template("registration.html")
	
@app.route("/add/user", methods=["POST"])
def addUser():
	response = {}
	if current_user.is_authenticated:
		email = request.form["email"]
		if email.strip():
			userEmail = email+"@ebizontek.com"
			u = User.query.filter_by(email=userEmail).first()
			if u is None:
				user = User(email=userEmail)
				db.session.add(user)
				db.session.flush()
				role = Roles(user_id=user.id, role="Lead")
				db.session.add(role)
     			db.session.commit()
     			response["success"] = True
     			response["message"] = "You have added a user by email "+userEmail
     			return jsonify(**response)
     		else:
     			response["success"] = False
     	  		response["message"] = userEmail+" Already Present"
     	        return jsonify(**response) 	
   	else:
    	  response["success"] = False
     	  response["message"] = "You are not allowed to do that"
     	  return jsonify(**response)		


@app.route("/delete/user", methods=["POST"])
def deleteUser():
	response = {}
	id = request.form["id"]
	if current_user.is_authenticated:
		if id.strip():
			user = User.query.filter_by(id=id).first()
			role = Roles.query.filter_by(user_id=id).first()
			if user is not None and role is not None:
				db.session.delete(user)
				db.session.delete(role)
				db.session.commit()
				response["success"] = True
				response["message"] = "User Deleted Successfully"
				return jsonify(**response)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))     		

