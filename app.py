#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, jsonify, render_template, request
import re
import storage


app = Flask(__name__)


def validate_user_input(fname, lname, code, phone, country, city, gender):
    """ Validates user info input """
    errors = {}
    if len(fname) < 3 or not re.search("^[a-zA-Z]+$", fname):
        errors["firstname"] = "Firstname has few chracters"
    if len(lname) < 3 or not re.search("^[a-zA-Z]+$", lname):
        errors["lastname"] =  "Lastname cant be empty or has less characters"
    if len(code) < 1 or not re.search("^[0-9]+$", code):
        errors["country_code"] = "invalid country code"
    if len(phone) < 5 or not re.search("^[0-9]+$", phone):
        errors["phone_number"] = "Invalid phone number"
    if len(country) < 3 or not re.search("[a-zA-Z]+", country):
        errors["country"] = "Country name is invalid"
    if len(city) < 3:
        errors["city"] = "city name is invalid"
    if len(gender) < 3 or not re.search("[a-zA-Z]+", gender):
        errors["gender"] = "the gender in invalid"
    
    return errors



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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)