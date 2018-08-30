from flask import Flask, render_template
from Model.Server import User, Instances


app = Flask(__name__)


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/login")
def register():
	return render_template("login.html")


@app.route("/admin")
def admin():
	return render_template("admin.html")