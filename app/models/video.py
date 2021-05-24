from flask import current_app
from app import db
from flask import Blueprint
from datetime import datetime

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    release_date = db.Column(db.Date)
    total_inventory = db.Column(db.Integer)
    #video = db.relationship('Rental', backref="rentals", lazy=True)