#!/usr/bin/python3
"""
Implements a structure to hold phone numbers and related info
"""
import pytz
from datetime import datetime
from tzlocal import get_localzone
from storage import db


class PhoneNumber:
    """
    A node that holds phone number and country code 
    """
    next = None
    number = None
    code = None
    timezone = None


class NumbersList:
    """
    Implements a singly linked list of phone numbers
    """
    def __init__(self):
        """ Sets the head pointer to None"""
        self.head = None
    
    def create_node(self, phone, code):
        """
        Appends a node to the linked list

        Args:
            node: an instance of PhoneNumber representing a node

        Returns:
            node (PhoneNumber): a  PhoneNumber node instance
        """
        node = PhoneNumber()
        node.code = code
        node.number = phone
        return node
    
    def is_greater_equal(self, node_1, node_2):
        """ 
        Finds if current datetime of node_1 is greater or equal to that
        of node_2 by getting the timezones of the nodes and converting
        to current timezone and then compares the datetime

        Args:
            node_1: PhoneNumber instance with timezone attribute
            node_2: PhoneNumber instance with timezone attribute

        Returns:
            True or False: True if node_1 datetime is greater that node_2
                           else false
        """
        current_dt = datetime.now()

        node1_tz = pytz.timezone(node_1.timezone)
        node2_tz = pytz.timezone(node_2.timezone)

        node_1_dt = current_dt.astimezone(node1_tz).astimezone(pytz.utc)
        node_2_dt = current_dt.astimezone(node2_tz).astimezone(pytz.utc)

        print("node_1 => {}".format(node_1_dt))
        print("node_2 => {}".format(node_2_dt))
        print("node_1 is greater than node 2 => {}".format(node_1_dt > node_2_dt))

        return node_1_dt >= node_1_dt
        


        
    def create_list(self):
        """ Create a sorted list of phone_numbers based on timezone"""
        numbers = db.get_all_numbers()

        if numbers:
            if self.head:
                current = self.head
                while current:
                    dt = datetime.now()
                    for code, number, timezone in numbers:
                        cdtz = dt.astimezone(pytz.timezone(timezone))
                    



node1 = PhoneNumber()
node1.timezone = "Pacific/Auckland"

node2 = PhoneNumber()
node2.timezone = str(get_localzone())

nl = NumbersList()

print("node 1 {} => {}".format(node1.timezone, datetime.now().astimezone(pytz.timezone(node1.timezone)).astimezone(get_localzone())))
print("node 2 {} => {}".format(node2.timezone, datetime.now().astimezone(pytz.timezone(node2.timezone)).astimezone(get_localzone())))

print(nl.is_greater_equal(node1, node2))

    





