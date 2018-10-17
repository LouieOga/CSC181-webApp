from flask import Flask, render_template, request
from controller import *

@app.route('/', methods = ['GET'])
def index():
	return render_template("index.html")

@app.route('/signup', methods = ['GET','POST'])
def signup():
	return render_template("register.html")

@app.route('/signin', methods = ['GET'])
def signin():
	return render_template("login.html")