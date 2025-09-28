#!/usr/bin/bash
# starts a flask web app with necessary data

# API Keys
export APIIP_API_KEY=617ddb8f-f252-40a6-a723-1ab3e433f8be
export WEATHERBIT_API_KEY=bb732992d09e4a0bbb7f9e2c62996ad7

# Application Configuration
export FLASK_ENV=development
export FLASK_DEBUG=true
export PORT=5000

# Start the Flask application
python app.py  
