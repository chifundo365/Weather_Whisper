#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template, request, jsonify
import os
from uuid import uuid4
from datetime import datetime
from process_data import ProcessData


app = Flask(__name__)

@app.route("/", strict_slashes=False, methods=["GET"])
def homepage():
    """
    Route for the default homepage of the site
    """
    id  = uuid4()
    
    if os.environ.get("load_balancer") == "yes":
        forwarded_for = request.headers.get("X-Forwarded-For")
        ip_address = forwarded_for.split(',')[0].strip()
    else:
        ip_address = request.remote_addr
    
    print("ip_address", ip_address)
   
    location = ProcessData.geolocation(ip_address)
    
    if location is None or not location.get('success', False):
        # fallback: use default coordinates (e.g., Accra, Ghana)
        latitude = 5.6037
        longitude = -0.1870
        country = "Ghana"
        country_code = "GH"
        print("Using fallback location: Ghana")
    else:
        latitude = location.get("latitude")
        longitude = location.get("longitude")
        country = location.get('countryName')
        country_code = location.get('countryCode')
        print(f"Using API location: {country} ({latitude}, {longitude})")

    weather = ProcessData.get_weather(latitude, longitude)
    print("Weather data:", weather)
    
    # Handle weather API failures with fallback data
    if not weather or not weather.get('success', False):
        print("Weather API failed, using fallback weather data")
        weather = {
            'success': True,
            'data': [{
                'temp': 25,
                'weather': {'description': 'Clear sky', 'icon': '01d'},
                'wind_spd': 3.2,
                'rh': 65,
                'pres': 1013,
                'vis': 10,
                'uv': 5,
                'app_temp': 27
            }]
        }
    
    forecasts_data = ProcessData.get_forecasts(latitude, longitude)
    if forecasts_data and forecasts_data.get('success', False) and 'data' in forecasts_data:
        forecasts = forecasts_data.get('data', [])[1:8]
    else:
        print("Forecast API failed, using fallback forecast data")
        forecasts = []

    # Safely process forecasts
    for forecast in forecasts:
        try:
            if 'valid_date' in forecast:
                dt = datetime.strptime(forecast['valid_date'], '%Y-%m-%d')
                forecast['valid_date'] = (dt.strftime("%A"))
        except (ValueError, KeyError) as e:
            print(f"Error processing forecast date: {e}")
            continue

    return render_template(
        "index.html",
        weather=weather,
        id=id,
        country=country,
        country_code=country_code,
        forecasts=forecasts
    )


@app.route("/subscribe", methods=["GET"], strict_slashes=False)
def subscribe():
    """ subscribe page - shows coming soon message """
    return render_template("subscribe.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
