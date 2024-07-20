#!/usr/bin/python3
"""
Implements a structure to hold phone numbers and related info
"""
from storage import db


class PhoneNumber:
    """
    A node that holds phone number and country code 
    """
    next = None
    prev = None
    number = None
    code = None


class NumbersList:
    """
    Implements a doubly linked list of phone numbers
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
        
    def create_list(self):
        """ Create a sorted list of phone_numbers based on timezone"""
        numbers = db.get_all_numbers()

        if numbers:
            if self.head == None:
                for code, number in numbers:
                    


    





