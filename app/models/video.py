from flask import current_app
from app import db
from flask import Blueprint
from datetime import datetime

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50))
    release_date = db.Column(db.DateTime)
    total_inventory = db.Column(db.Integer)
    #video = db.relationship('Rental', backref="rentals", lazy=True)


    def make_json(self):
            return {
                "id": self.id,
                "title": self.title,
                "release_date": self.release_date,
                "total_inventory": self.total_inventory
                #"available_inventory": self.available_inventory
            }

    def from_json(request_data):
            new_video = Video(
                title = request_data["title"],
                release_date = request_data["release_date"],
                total_inventory = request_data["total_inventory"]
            )
            return new_video