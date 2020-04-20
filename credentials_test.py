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

    def tearDown(self):
        """
        the tearDown method will help to clean up after every test case is run 
        """
        credentials.credentials_list = []

    def test_init(self):
        """
        testcase: testing to see whether object is well initialised
        """
        self.assertEqual( self.new_credentials.user_password, "pete")
        self.assertEqual( self.new_credentials.credentials_name, "gmail")
        self.assertEqual( self.new_credentials.credentials.credentials_password, "gmail08")
        