#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template, request, abort, url_for, jsonify, redirect
from uuid import uuid4
import storage
from process_data import ProcessData


app = Flask(__name__)

@app.route("/", strict_slashes=False, methods=["GET"])
def homepage():
    """
    Route for the default homepage of the site
    """
    id  = uuid4()
    if request.method == "GET":
        return render_template("index.html", id=id)


@app.route("/subscribe", methods=["GET"], strict_slashes=False)
@app.route("/subscribe/<form_id>/",  methods=["GET"], strict_slashes=False)
def subscribe(form_id=None):
    id = uuid4()
    """ subscribe page """
    if form_id is not None:
        try:
            data = request.args
            if storage.db.create(**data):
                return "success"
            abort(500)
        except Exception  as e:
            print(e)
            abort(500)       
    else:
         return render_template("subscribe.html")

@app.route("/validate_form", strict_slashes=False, methods=["POST"])
def validate_form():
     """
     Validates user form input fields

     Returns:
        dict : an empy dictionary if no errors else a dict with fields and 
               their corresponding errors
     """
     try:
            data = dict(request.form)
            print(data)
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            data['timezone'] = ProcessData.get_time_zone(latitude, longitude)
            validate_data = ProcessData.validate_user_input(data)

            if validate_data:
                return redirect(url_for("subscribe", form_id=uuid4(), **data))
            else:
                 return jsonify(validate_data)
     except Exception as e:
            error = {"server_error": e}
            return jsonify(error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
