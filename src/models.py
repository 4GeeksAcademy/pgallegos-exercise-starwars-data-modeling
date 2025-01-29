import os
import sys
from sqlalchemy import ForeignKey
from eralchemy2 import render_er 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import enum

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True, nullable=False)

class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    external_id = db.Column(db.String(50))
    name = db.Column(db.String(50))
    user_id = db.Column(db.Integer, ForeignKey('user.id'), nullable=False)
    type = db.Column(db.Enum('Species', 'Planets', 'People'))

class Species(db.Model):
    __tablename__ = 'species'
    uid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    name = db.Column(db.String(50))
    homeworld = db.Column(db.Integer, ForeignKey('planets.uid'), nullable=False)
    classification = db.Column(db.String(50))

class Planets(db.Model):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    uid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    gravity = db.Column(db.String(250))
    
class People(db.Model):
    __tablename__ = 'people'
    uid = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250))
    name = db.Column(db.String(50))
    homeworld = db.Column(db.Integer, ForeignKey('planets.uid'), nullable=False)


## Draw from SQLAlchemy base
try:
    result = render_er(db.Model, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e