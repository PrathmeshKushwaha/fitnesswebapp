from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

class User(db.Model):
    __tablename__ = 'user'
    uid = db.Column(db.Integer, primary_key=True)
    uname = db.Column(db.String)
    uemail = db.Column(db.String)
    uphone = db.Column(db.String)
    city = db.Column(db.String)
    gender = db.Column(db.String)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    profile = db.relationship('Profile', back_populates='user')
    posts = db.relationship('Posts', back_populates='user')
    udata = db.relationship('UserData', back_populates='user')
    agenda = db.relationship('Agenda', back_populates='user')
    explore = db.relationship('Explore', back_populates='user')
    message = db.relationship('Message', back_populates='user')

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/Dashboard.html')
def dashboard():
    return render_template('Dashboard.html')

with app.app_context():
    db.create_all()