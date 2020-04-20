"""
credentials Module 

To generate passwords from python, import string and random modules 

import user from user module to get access to user 
"""

from random import choice 
import string 
# from user import User 

"""
credentials class to create instances of the user's credentials 
"""

class Credentials:
    """
    this is a class that generates instances of credentials for the user
    """

    # start 
    credentials_list = [] # Empty list of the credentials

    def __init__(self, user_password, credentials_name, credentials_password):
        """
        __init__ method to  specify the attributes of a User object
        
        Args:
            user_password = user password
            credentials_name = the name of the credentials acccount
            credentials_password = the password of the account
        """
        self.user_password = user_password
        self.credentials_name = credentials_name
        self.credentials_password = credentials_password