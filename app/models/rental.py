from flask import current_app
from app import db
from flask import Blueprint
from datetime import datetime, timedelta

class Rental(db.Model):
    __tablename__ = 'rentals'
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), primary_key=True)
    video_id = db.Column(db.Integer, db.ForeignKey('videos.id'), primary_key=True)
    due_date = db.Column(db.Date)
    customer = db.relationship("Customer", backref="rental", lazy=True)
    video = db.relationship("Video", backref="rental", lazy=True)

    
    def make_json_check_out(self):
    
        return {
            "customer_id": self.customer_id,
            "video_id": self.video_id,
            "due_date": self.due_date
        }
    
    def make_json_customer_renters(self):

        return {
        "due_date": self.due_date,
        "name": self.customer.name,
        "phone": self.customer.phone,
        "postal_code": self.customer.phone
    }

    #class methods 
    # def from_json(request_data):

    #     now = datetime.now()
    #     due = timedelta(days=+7)
    #     due_date = now + due   

    #     new_rental = Rental(
    #         customer_id = request_data["customer_id"],
    #         video_id = request_data["video_id"], 
    #         due_date = due_date
    #     )

    #     return new_rental