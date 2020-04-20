"""
User Module

import credentials from credentials 

import pyperclip to allow copying to the clipboard
"""

import credentials from credentials

"""
User class to allow users creat a password locker account
"""

class User:
    """
    Class that generates new instances of user accounts 
    """

    # start 
    contact_list = [] # Empty user list 
    def __init__(self,user_name,user_password):

        '''
        __init__ method to define the properties of a User object

        Args:
            user_name : the name of the user 
            user_password : the user's password
        '''

        self.user_name = first_name
        self.user_password = user_password

    def save_user(self):
        """
        way of saving a user to the user list
        """
        User.user_list.append(self)

