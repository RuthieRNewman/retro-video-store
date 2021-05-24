from flask import current_app
from app import db
from flask import Blueprint

class Rental(db.Model):
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), primary_key=True)
    due_date = db.Column(db.Date)
    customer = db.relationship("Customer", backref="rental", lazy=True)
    video = db.relationship("Video", backref="rental", lazy=True)