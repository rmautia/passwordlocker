"""
credentials Module 

To generate passwords from python, import string and random modules 

import user from user module to get access to user 
"""

from random import choice 
import string 
from user import User 

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

    def save_credentials(self):
        """
        methos thriugh wich the application saves the user credentials to credentials list
        """
        credentials.credentials_list.append(self)
        
    #generating password for the user 
    @classmethod
    def generate_password(cls):
        """
        this method will generate a random alphanumeric password for the user 
        """
        #length of password to be generated 
        size = 10
        
        # random alphanumeric generation
        alphanumeric = string.ascii_lowercase + string.digits + string.ascii_uppercase

        #now to create the password
        password = "".join( choice(alphanumeric) for num in range(size))

        return password

    # method to display the credentials
    @classmethod
    def display_credentials(cls, password):
        """
        method that will return the credentials list

        Args:
            password  : the user password
        """
        user_credentials_list = []
        
        for credentials in cls.credentials_list:
            if credentials.user_password == password:
                user_credentials_list.append(credential)

        return user_credentials_list

    @