#!/usr/bin/python3
""" Implements a connecttion to the mysql database """
import mysql.connector
from os import environ


class DB_storage():
    db = ""
    cursor = ""

    def __init__(self):
        """ Creates a connection to the myqsql database """
        try:
            host = environ.get("host")
            user = environ.get("user")
            password = environ.get("password")
            database = environ.get("db")
            self.db = mysql.connector.connect(
                    host=host,
                    user=user,
                    password=password,
                    db=database,
                    port=3306
                    )
            self.cursor = self.db.cursor()
        except Exception as e:
            print(e)

    def get_all_numbers(self):
        """ Gets all the phone numbers wih country code in the database """
        if self.cursor:
            query = "SELECT country_code, phone_number FROM users"
            self.cursor.execute(query)

            return self.cursor.fetchall()
        return ()

    def create(self, fname, lname, c_code, phone, country, city, gender):
        """ Inserts into DB storage current users personal info """
        query = "INSERT INTO users({}) VALUES(%s, %s, %s, %s, %s, %s, %s)"
        fields = "first_name, last_name, country_code, {}, {}, {}, {}"
        fields.format("phone_number", "country", "city", "gender")
        query.format(fields)
        result = self.cursor.execute(
                query, (
                    fname,
                    lname,
                    c_code,
                    phone,
                    country,
                    city,
                    gender
                    )
                )
        return True if result else False
