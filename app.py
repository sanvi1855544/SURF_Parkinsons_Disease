
from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import requests
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash



app = Flask(__name__, template_folder="templates", static_folder = "static")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


    
class User(db.Model):
    __tablename__ = 'user_list'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    
    def make_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def auth_password(self, password):
        return check_password_hash(self.password_hash, password)

with app.app_context():    
    db.create_all()


@app.route("/")
def index():
    response = requests.get('http://worldtimeapi.org/api/ip')
    if response.status_code == 200: 
        times = response.json()
        live_time = times['datetime']
        return render_template('index.html', time=live_time)
    return "Couldn't get time from API"

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and user.auth_password(password):
            return redirect('/therapy')
        else:
            return render_template("login.html")
    if request.method == 'GET':
        return render_template('login.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if User.query.filter_by(username=username).first():
            error_message = 'Sorry, this username already exists'
            return render_template('register.html', error_message=error_message)
        else:
            new_user = User(username=username)
            new_user.make_password(password)
            
            db.session.add(new_user)
            db.session.commit()
            
            return redirect('/therapy')
    if request.method == 'GET':   
        return render_template("register.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/instructions")
def instructions():
    return render_template("instructions.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/therapy")
def therapy():
    return render_template('therapy.html')

@app.route("/words")
def words():
    return render_template('words.txt')

@app.route("/sentences")
def sentences():
    return render_template('sentences.txt')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)