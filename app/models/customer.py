from flask import current_app
from app import db
from flask import Blueprint
from datetime import datetime

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    registered_at = db.Column(db.DateTime, nullable=False)
    rentals = db.relationship("Rental", backref="customers", lazy=True)

    def make_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "registered_at": self.registered_at,
            "postal_code": self.postal_code,
            "phone": self.phone,
            "videos_checked_out_count": 0
        }
    
    def from_json(request_dict):
        new_customer = Customer(
            name = request_dict["name"],
            registered_at = datetime.now(),
            postal_code = request_dict["postal_code"],
            phone = request_dict["phone"]
        )
        return new_customer

    def rental_response(customer_id):

        customer = Customer.query.get(customer_id)
        rented_videos =customer.rentals
        rentals_response = []

        for video in rented_videos:
            video_data = {}
            video_data['title'] = video.title
            video_data['release_date'] = video.release_date
            video_data['due_date'] = video.due_date

            rentals_response.append(video_data)
        
        return rentals_response