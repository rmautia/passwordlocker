import unittest
from random import choice 
import string 
#from user import User 

"""
credentials class to create instances of the user's credentials 
"""

class Credentials:
    """
    this is a class that generates instances of credentials for the user
    """

    # start 
    credentials_list = [] # Empty list of the credentials

    def __init__(self, user_password, credentials_name,credentials_email, credentials_password):
        """
        __init__ method to  specify the attributes of a User object
        
        Args:
            user_password = user password
            credentials_name = the name of the credentials acccount
            credentials_email = the email of the credentials account to be linked with the account
            credentials_password = the password of the account
        """
        self.user_password = user_password
        self.credentials_name = credentials_name
        self.credentials_email = credentials_email
        self.credentials_password = credentials_password

    def save_credentials(self):
        """
        method through which the application saves the user credentials to credentials list
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

        Args:credentials_email = the email of the credentials account to be linked with the account
            password  : the user password
        """
        user_credentials_list = []
        
        for credentials in cls.credentials_list:
            if credentials.user_password == password:
                user_credentials_list.append(credential)

        return user_credentials_list

    @classmethod
    def credentials_exist(cls, name):
        """
        method to check existense of a credentials
        
        Args
            name: name of credentials to be searched
        
        Returns:
            Boolean: true/ false subject to whether the credentials exist
        """

        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return True 

        return False 

    # deleting credentials
    @classmethod
    def delete_credentials(self):
        """
        method that deletes credentials account that user no longder needs
        """
        Credentials.credentials_list.remove(self)

    # paste with pyperclip
    @classmethod
    def copy_credentials_email(self):
        """
        method to copy credentials email to the clipboard
        """
        credentials_name = credentials.credentials_exists()
        pyperclip.copy(credentials_name.credentials_email)


    
if __name__ == '__main__':
    unittest.main()