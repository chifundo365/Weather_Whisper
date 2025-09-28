#!/usr/bin/python3
"""
Processes the data received and create new data based on the data receiveid
"""
import requests
import os


class ProcessData():
    """ 
    Proceses  and validates data got from user
    uses the data to make new valuable data
    """

    @staticmethod
    def geolocation(ip):
        """ Gets the geolocation with given data"""

        try:
            print(f"ip address supplied: {ip}")
            api_key = os.environ.get("APIIP_API_KEY")
            url = f"https://apiip.net/api/check?ip={ip}&accessKey={api_key}"
            print(f"URL being called: {url}")
            
            # Add timeout and SSL verification settings to handle connection issues
            r = requests.get(url, timeout=10, verify=True)
            print(f"Status code: {r.status_code}")
            print(f"Response: {r.text}")
            if r.status_code < 301:
                response = r.json()
                response["success"] = True
                return response
            else:
                print(f"API returned status code: {r.status_code}")
                return {"success": False, "msg": f"API error: {r.status_code}"}

        except Exception as e:
            print(f"Exception occurred: {e}")
            return {"success": False, "msg": "could not get your location data"}


    @staticmethod
    def get_weather(latitude, longitude):
        """
        Gets the current weather of a place

        Args:
            latitude: latitude of the place
            longitude: the longitude of the place

        Returns:
            dict: a dictionary containing the weather data
                  or a dictionary with error data
        """
        try:
            url = "https://api.weatherbit.io/v2.0/current"
            api_key = os.environ.get("WEATHERBIT_API_KEY")
            
            print(f"Weather API Key: {'SET' if api_key else 'NOT SET'}")
            print(f"Latitude: {latitude}, Longitude: {longitude}")

            data = {"lat": latitude, "lon": longitude, "key": api_key}
            print(f"Weather API URL: {url}")
            print(f"Weather API params: {data}")
            
            # Add timeout and SSL verification settings to handle connection issues
            res = requests.get(url, params=data, timeout=10, verify=True)
            print(f"Weather API Status code: {res.status_code}")
            print(f"Weather API Response: {res.text}")
            
            if res.status_code < 301:
                r = res.json()
                r["success"] = True
                return r
            else:
                return {
                        "success": False,
                        "msg": f"Weather API error: {res.status_code} - {res.text}"
                       }
        except Exception as e:
            print(f"Weather API Exception: {e}")
            return {"success": False, "msg": f"Could not get weather info: {str(e)}"}


    @staticmethod
    def get_time_zone(latitude, longitude):
        """
        Gets the timezone for given coordinates
        
        Args:
            latitude: latitude of the place
            longitude: longitude of the place
            
        Returns:
            str: timezone string or None if failed
        """
        try:
            # You can use a timezone API here or return a default
            # For now, returning a default timezone
            return "UTC"
        except Exception as e:
            print(f"Timezone API Exception: {e}")
            return "UTC"
        

    @staticmethod
    def get_forecasts(latitude, longitude):
        """
        Gets the current weather forecasts of a place in 16 days

        Args:
            latitude: latitude of the place
            longitude: the longitude of the place

        Returns:
            dict: a dictionary containing the forecasts data
                  or a dictionary with error data
        """
        try:
            url = "https://api.weatherbit.io/v2.0/forecast/daily"
            api_key = os.environ.get("WEATHERBIT_API_KEY")
            print('Forecast API Key:', api_key)
            data = {"lat": latitude, "lon":longitude, "key":api_key}
            # Add timeout and SSL verification settings to handle connection issues
            res = requests.get(url, params=data, timeout=10, verify=True)
            print(f"Forecast API Status code: {res.status_code}")
            print(f"Forecast API Response: {res.text}")
            if res.status_code < 301:
                r = res.json()
                r["success"] = True
                return r
            else:
                return {
                        "success": False,
                        "msg":"could not get your forecasts data"
                       }
        except Exception as e:
            return {"success": False, "msg": "could not get you forecasts info"}
