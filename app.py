#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, jsonify, render_template, request
import re
import storage


app = Flask(__name__)




@app.route("/", strict_slashes=False, methods=["GET", "POST"])
def home_page():
    """
    Route for the default homepage of the site
    Gets the user input from a form and inserts user info in db
    """
    if request.method == "GET":
        return render_template("index.html")

    first_name = request.form.get("fname")
    last_name = request.form.get("lname")
    country_code = request.form.get("c-code")
    phone_number = request.form.get("p-number")
    country = request.form.get("country")
    city = request.form.get("city")
    gender = request.form.get("gender")

    validate = validate_user_input(
            first_name,
            last_name,
            country_code,
            phone_number,
            country,
            city,
            gender
            )
    
    if validate == {}:
       storage.create_subscriber(
                first_name,
                last_name,
                country_code,
                phone_number,
                country,
                city,
                gender
                )
       return render_template("subscribe.html", errors=False)
    else:
        return render_template("subscribe.html", errors=validate)
