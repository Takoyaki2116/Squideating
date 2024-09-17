import re
from flask import Flask
from flask import render_template
from flask import redirect
from datebase import Turtles
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/login')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')

@app.route('/top')
def top():
  return render_template('top.html')

@app.route('/new', methods=['POST'])
def new():
  Turtles.create(name = request.form['username'], password = request.form['password'])
  return redirect('/login')
  


app.run(host='0.0.0.0', port=8080)