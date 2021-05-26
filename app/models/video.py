from types import ClassMethodDescriptorType
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
    rentals = db.relationship('Rental', backref="rentals", lazy=True)


    def make_json(self):

        currently_rented_out = len(self.rentals)
        total = self.total_inventory
        available = total - currently_rented_out

        return {
            "id": self.id,
            "title": self.title,
            "release_date": self.release_date,
            "total_inventory": self.total_inventory,
            "available_inventory": available
        }

    #@classmethod
    def from_json(request_data):

        date_time_str = request_data["release_date"]
        date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d')

        new_video = Video(
            title = request_data["title"],
            release_date = date_time_obj,
            total_inventory = request_data["total_inventory"] 
        )
        return new_video
    
    def rental_response(request_data):

        return {
                "title": request_data["title"],
                "release_date": request_data["release_date"],
                "due_date": request_data["due_date"] 
            }
