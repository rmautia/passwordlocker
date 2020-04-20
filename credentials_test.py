"""
test Module for password locker application

impoor unittest to create unittests for the application 
import the module to be tested from passwordlocker, in this case the credentials module
"""

import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    class for test that defines test cases for the credentials module

    Args:
        unittest.TestCase : test class for python that helps create test cases for the application 
    """
    def setUp(self):
        """
        set up method will run before each test case
        """
        # creating the credential object
        self.new_credentials = credentials("pete","gmail","gmail08")