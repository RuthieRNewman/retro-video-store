from app import db
from app.models.customer import Customer
from app.models.video import Video
from flask import request, Blueprint, make_response, jsonify
import os
import requests
from datetime import datetime


customer_bp = Blueprint("customers", __name__, url_prefix="/customers")

@customer_bp.route("", methods=["POST"], strict_slashes=False)
def create_new_customer():
    request_body = request.get_json()
    if not request_body:
        return make_response({"details": "Invalid Data"}, 400)
    
    new_customer = Customer.from_json(request_body)
    print(new_customer)

    db.session.add(new_customer)
    db.session.commit()

    return make_response({"customer": new_customer.make_json()}, 201)