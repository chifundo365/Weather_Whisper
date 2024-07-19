#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template, request
import storage
from process_data import ProcessData


app = Flask(__name__)




@app.route("/", strict_slashes=False, methods=["GET", "POST"])
def home_page():
    """
    Route for the default homepage of the site
    Gets the user input from a form and inserts user info in db
    """
    if request.method == "GET":
        return render_template("index.html")
    
    try:
        data = request.form
        data['timezone']
        validate_data = ProcessData.validate_user_input(data)

        if len(validate_data) == 0:
            storage.db.create(**data)
            return render_template("subscribe.html", errors=False)
        else:
            return render_template("subscribe.html", errors= validate_data)

    except Exception as e:
        return render_template("subscribe.html", errors=True)
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)