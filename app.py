from flask import Flask, render_template
from Model.Server import User, Server


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/admin")
def admin():
	return render_template("admin.html")