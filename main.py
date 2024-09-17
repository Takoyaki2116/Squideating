import re
from flask import Flask
from flask import render_template
from flask import redirect
from datebase import Turtles
from flask import request

from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(user_id):
    return Turtles.get_or_none(Turtles.id == int(user_id))

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
  Turtles.create(username = request.form['username'], password = request.form['password'])
  return redirect('/login')

@app.route('/go', methods=['POST'])
def go():
  username = request.form['username']
  password = request.form['password']
  turtles = Turtles.get_or_none(Turtles.username == username)
  if turtles and turtles.password == password:
   login_user(turtles)
   return redirect('/top')


app.run(host='0.0.0.0', port=8080)