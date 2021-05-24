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

    return make_response(new_customer.make_json(), 201)

@customer_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_customers():
    customers = Customer.query.all()

    customers_response = [customer.make_json() for customer in customers]


    return make_response(jsonify(customers_response),200)


@customer_bp.route("/<customer_id>", methods=["GET"], strict_slashes=False)
def get_customer_by_id(customer_id):
    customer = Customer.query.get(customer_id)

    if customer is None:
        return make_response("", 404)
    
    return make_response(customer.make_json(), 200)

@customer_bp.route("/<customer_id>", methods=["PUT"], strict_slashes=False)
def update_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if customer is None:
        return make_response("", 404)
    
    request_data = request.get_json()
    customer.name = request_data["name"]
    customer.postal_code = request_data["postal_code"]
    customer.phone = request_data["phone"]

    db.session.commit()
    return make_response(customer.make_json(), 200)

@customer_bp.route("/<customer_id>", methods=["DELETE"], strict_slashes=False)
def delete_customer():
    pass

