from flask import current_app
from app import db
from flask import Blueprint

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    postal_code = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    registered_at = db.Column(db.DateTime, nullable=False)
    #customer = relationship("Rental", backref="customers", lazy=True)