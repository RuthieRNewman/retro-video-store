from app import db
from app.models.customer import Customer
from app.models.video import Video
from flask import request, Blueprint, make_response, jsonify
import os
import requests
from datetime import datetime


customer_bp = Blueprint("customers", __name__, url_prefix="/customers")
video_bp = Blueprint("videos", __name__, url_prefix="/videos")

@customer_bp.route("", methods=["POST"], strict_slashes=False)
def create_new_customer():
    request_body = request.get_json()
    print(request_body)

    if not request_body:
            return make_response({"details": "Invalid data"}, 400)
    
    
    if not request_body.get("name"): 
        return make_response({"details": "Please enter a value for Name"}, 400)
    elif not request_body.get("postal_code"):
        return make_response({"details": "Please enter a value for postal code"}, 400)
    elif not request_body.get("phone"):
        return make_response({"details": "Please enter a value for phone"}, 400)

    new_customer = Customer.from_json(request_body)

    db.session.add(new_customer)
    db.session.commit()

    return make_response({"id": f"{new_customer.id}"}, 201)

@customer_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_customers():
    customers = Customer.query.all()

    if customers is None:
        return make_response([], 404)

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
        return make_response({"details": f"Customer {customer_id} not found"}, 404)
    
    request_data = request.get_json()
    if not request_data.get("name") or type(request_data.get("name")) != str:
        return make_response({"details": "Name field is missing or of an invalid data type"}, 404)
    elif not request_data.get("postal_code") or type(request_data.get("postal_code")) != str:
        return make_response({"details": "Postal_code field is missing or of an invalid data type"}, 404)
    elif not request_data.get("phone") or type(request_data.get("phone")) != str:
        return make_response({"details": "Phone number field is missing or of an invalid data type"}, 404)
    
    customer.name = request_data["name"]
    customer.postal_code = request_data["postal_code"]
    customer.phone = request_data["phone"]

    db.session.commit()
    return make_response(customer.make_json(), 200)

@customer_bp.route("/<customer_id>", methods=["DELETE"], strict_slashes=False)
def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)

    if customer is None:
        return make_response("", 404) 

    db.session.delete(customer)
    db.session.commit()

    return make_response({"id": f"{customer.id}"}, 200)   


#video routes

@video_bp.route("", methods=["POST"], strict_slashes=False)
def create_new_video():
    request_data = request.get_json()

    if not request_data:
        return make_response({"details": "Invalid Data"}, 400)
    
    if not request_data.get("title") or type(request_data.get("title") != str):
        return make_response({"details": "Invalid Data"}, 400)
    #release date is datetime?
    elif not request_data.get("release_date") or type(request_data.get("release_date")) != datetime:
        return make_response({"details": "Invalid Data"}, 400)
    elif not request_data.get("total_inventory")  or type(request_data.get("total_inventory")) != int:
        return make_response({"details": "Invalid Data"}, 400)
        
    new_video = Video.from_json(request_data)

    db.session.add(new_video)
    db.session.commit()

    return make_response({"id": f"{new_video.id}"}, 201)

    

@video_bp.route("", methods=["GET"], strict_slashes=False)
def get_all_videos():
    videos = Video.query.all()

    if videos is None:
        return make_response([], 200)

    video_response = [video.make_json() for video in videos]

    return make_response(jsonify(video_response),200)


@video_bp.route("/<video_id>", methods=["GET"], strict_slashes=False)
def get_video_by_id(video_id):
    video = Video.query.get(video_id)

    if video is None:
        return make_response({"details": f"Video with id : {video_id} not found"}, 404)

    return make_response(video.make_json(), 200)


@video_bp.route("/<video_id>", methods=["PUT"], strict_slashes=False)
def update_video_by_id(video_id):
    video = Video.query.get(video_id)
    request_data = request.get_json()

    if video is None:
        return make_response("", 404)
    
    if not request_data.get("title") or type(request_data.get("title")) != str:
        return make_response({"details": "Please enter a valid value for title field."}, 400)
    elif not request_data.get("release_date") or type(request_data.get("release_date")) != datetime:
        return make_response({"details": "Please enter a valid value for release_date field."}, 400)
    elif not request_data.get("total_inventory")  or type(request_data.get("total_inventory")) != int:
        return make_response({"details": "Please enter a valid value for total_inventory field."}, 400)
    
    request_data = request.get_json()

    #do i need a condtional for this put

    video.title = request_data["title"]
    video.release_date = request_data["release_date"]
    video.total_inventory = request_data["total_inventory"]

    db.session.commit()

    return make_response(video.make_json(), 200)


@video_bp.route("/<video_id>", methods=["DELETE"], strict_slashes=False)
def delete_video(video_id):
    video = Video.query.get(video_id)

    if video is None:
        return make_response({"details": f"Video id number: {video_id} not found"}, 404)

    db.session.delete(video)
    db.session.commit()

    return make_response({"id": f"{video.id}"}, 200)