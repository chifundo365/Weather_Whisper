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
    def validate_user_input(*args, **kwargs):
        """
        Validates user info input

        Args:
            args (tuple): list of arguments(unused)
            kwargs (dict): key value pairs of input fields

        Returns:
            a dict with fields and the associated errors or
            an empty dict if no errors 
        """
        import re


        field_re = {
                "user_name": r"^[a-zA-Z]+$",
                "country_code": r"^[0-9]+$",
                "phone_number": r"^[0-9]+$",
                "country": r"^[a-zA-Z]*",
                "city": r"^[a-zA-Z]*",
                "gender": r"^[a-zA-Z]+$",
                "longitude": r"^[0-9]+$",
                "latitude": r"^[0-9]+$"
                }
        errors = {}

        for  field in field_re.keys():
            if field not in kwargs.keys():
                errors[field] = "Missing {}".format(field)
            elif not re.match(field_re.get(field), kwargs.get(field)):
                errors[field] = "{} is invalid".format(field)
        
        return errors
    
    @staticmethod
    def get_time_zone(latitude, longitude):
        """
        Gets the timezone of a place

        Args:
            latitude - the latitude of the place
            longitude - longitude of the place
        
        Return: (string) timezone
        """
        import requests

        headers = {"accept": "application/json"}
        params = {"latitude": latitude, "longitude": longitude}
        url = "https://timeapi.io/api/TimeZone/coordinate"
        
        
        try:
            r = requests.get(url, headers=headers, params=params)
            if r.status_code == 200:
                return r.json().get("timeZone")
        except Exception as e:
            return {"error": e}

    @staticmethod
    def geolocation(ip):
        """ Gets the geolocation with given data"""

        try:
            print("trying")
            url = "https://apiip.net/api/check"
            data = {"ip": ip, "accessKey": os.environ.get("APIIP_API_KEY")}
            r = requests.get(url, params=data)
            print(r)
            if r.status_code < 301:
                response = r.json()
                response["success"] = True
                return response

        except Exception as e:
            return {"success": False, "msg": "colud not get your location data"}


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
            print(api_key)
            data = {"lat": latitude, "lon":longitude, "key":api_key}
            res = requests.get(url, params=data)
            
            print(res)
            if res.status_code < 301:
                r = res.json()
                r["success"] = True
                return r
            else:
                return {
                        "success": False,
                        "msg":"could not get your weather data"
                       }
        except Exception as e:
            return {"success": False, "msg": "could not get you weather info"}



     

