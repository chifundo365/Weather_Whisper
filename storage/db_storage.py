#!/usr/bin/python3
""" Implements a connecttion to the mysql database """
import mysql.connector
from os import environ


class DB_storage():
    """
    implements the database storage
    """
    db = None
    cursor = None

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
            return None
        
    def exists(self, code, phone_number):
        """
        Checks if a number exists in database

        Args:
            code (str): country code.
            phone_number(str): phone number.

        Returns:
            True or False: True if exists else False
        """
        q = "SELECT id  FROM users WHERE {}"
        query = q.format("country_code = %s AND phone_number = %s")
        self.cursor.execute(query, (code, phone_number))

        result = self.cursor.fetchone()

        return True if result else False

    def get_all_numbers(self):
        """
        Gets all the phone numbers wih country code in the database

        Returns:
            tuple: a tuple containing country_code, phone_numbers pairs.
                    or an empty tuple if empty
        """
        if self.cursor:
            query = "SELECT country_code, phone_number FROM users"
            self.cursor.execute(query)
            numbers_code = self.cursor.fetchall()

            return numbers_code
        return ()

    def create(self, *args, **kwargs):
        """
        Inserts into DB storage current users personal info

        Args:
            args: not used
            kwargs (dict): key value pairs of input fields
        
        Returns:
            True or False: True if inserted the new data otherwise False 
        """
 
        try:
            columns = ", ".join(list(kwargs.keys()))
            values = tuple(kwargs.values())
            placeholders = "%s, %s, %s, %s, %s, %s, %s, %s, %s"
            q = "INSERT INTO users({}) VALUES({})"
            query = q.format(columns, placeholders)

            result = self.cursor.execute(query, values)
            self.db.commit()
            return True if result else False
        except Exception as e:
            return False
