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

    def is_timezone_greater(self, node_1, node_2):
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

        node_1_dt = current_dt.astimezone(node1_tz).astimezone(node1_tz)
        node_2_dt = current_dt.astimezone(node2_tz).astimezone(node2_tz)

        nd1_tzoff = node_1_dt.strftime("%z")
        nd2_tzoff = node_2_dt.strftime("%z")

        return nd1_tzoff > nd2_tzoff




    def create_list(self):
        """ Create a sorted list of phone_numbers based on timezone"""
        numbers = db.get_all_numbers()
        for code, number, timezone in numbers:
            new_node = create_node(code, phone, timezone)
            if is_timezone_greater(current, new_node):
                    if previous:
                        previous.next = new_node
                        new_node.next = current
                    else:
                        new_node.next = current
                       self.head = new_node
                    break
                else:
                    previous = current
                    if current.next:
                        current = current.next
                    else:
                        previous.next = new_node
                        break






