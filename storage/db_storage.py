#!/usr/bin/python3
""" Implements a connecttion to the mysql database """
import MySQLdb
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
            db = MySQLdb.connect(
                    host=host,
                    user=user,
                    passwd=password,
                    db=database
                    )
            self.cursor = db.cursor()
        except Exception as e:
            return None

    def get_all_numbers(self):
        """ Gets all the phone numbers wih country code in the database """
        if self.cursor:
            query = "SELECT country_code, phone_number FROM users"
            result = self.cursor.execute(query)
            numbers_code = self.cursor.fetchall()

            return numbers_code
        return ()

    def create(self, fname, lname, c_code, phone, country, city, gender):
        """ Inserts into DB storage current users personal info """
        try:
            query = "INSERT INTO users({}) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            fields = "first_name, last_name, country_code, {}, {}, {}, {}"
            fields = fields.format("phone_number", "country", "city", "gender")
            query = query.format(fields)
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
            self.db.commit()
        except Exception as e:
            print(e)
            return None
