#!/usr/bin/python3
"""
Processes the data received and create new data based on the data receiveid
"""


class ProcessData:
    """ 
    Proceses  and validates data got from user
    uses the data to make new valuable data
    """

    def validate_user_input(self, *args, **kwargs):
        """ Validates user info input """
        import re


        field_re = {
                "first_name": "^[a-zA-Z]+$",
                "last_name": "^[a-zA-Z]+$",
                "country_code": "^[0-9]+$",
                "phone_number": "^[0-9]+$",
                "country": "^[a-zA-Z]*",
                "city": "^[a-zA-Z]*",
                "gender": "^[a-zA-Z]+$",
                "longitude": "^[0-9]+$",
                "latitude": "^[0-9]+$"
                }
        errors = {}

        for  field in field_re.keys():
            if field not in kwargs.keys():
                errors[field] = "Missing {}".format(field)
            elif not re.search(field_re.get(field), field):
                errors[field] = "{} is invalid".format(field)
        
        return errors

    def get_time_zone(self, latitude, longitude):
        """
        Gets the timezone of a place

        attr:
            latitude - the latitude of the place
            longitude - longitude of the place
        
        Return: (string) timezone
        """
        import requests

        headers = {"accept": "application/json"}
        params = {"latitude": latitude, "longitude": longitude}
        url = "https://timeapi.io/api/TimeZone/coordinate"
        
        r = requests.get(url, headers=headers, params=params)

        return r.json().get("timeZone")



