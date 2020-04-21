import unittest # Importing the unittest module
from credentials import Credentials # Importing the Credentials  class


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
        self.new_credentials = Credentials("pete","gmail","gmail08")

    def tearDown(self):
        """
        the tearDown method will help to clean up after every test case is run 
        """
        Credentials.credentials_list = []

    def test_init(self):
        """
        testcase: testing to see whether object is well initialised
        """
        self.assertEqual( self.new_credentials.user_password, "pete")
        self.assertEqual( self.new_credentials.credentials_name, "gmail")
        self.assertEqual( self.new_credentials.credentials_password, "gmail08")

    def test_save_credentials(self):
        """
        test to see whether user is saved to user list
        """
        
        self.new_credentials.save_credentials()

        self.assertEqual( len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        """
        test case: checking to see if multiple credentials can be saved to credentials list
        """

        generated_password = self.new_credentials.generated_password()

        self.assertEqual ( len(generated_password), 10)
    
    def test_display_credentials(self):
        """
        test to see if user can list all saved credentials
        """

        #saving the new credentials 
        self.new_credentials.save_credentials()

        test_credentials = Credentials("john", "outlook", "outlook12")

        test_credentials.save_credentials()

        test_credentials = Credentials("john", "glassdoor","glassy05")

        test_credentials.save_credentials()

        self.assertEqual( len(Credentials.display_credentials("john")), 2)

    def test_credentials_exist(self):
        """
        Test to check if we can return boolean for credentials not found
        """

        self.new_credentials.save_credentials()

        test_credentials = Credentials("john","outlook","outlook12") # new credentials

        test_credentials.save_credentials()

        # with use of contact exist method
        credentials_exists = Credentials.credentials_exists("outlook")

        self.assertTrue(credentials_exists)

    # deleting a credentials account
    def test_delete_credentials(self):
        """
        this method enables user to remove credentils the he/she no longer needs
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("Test","outlook","outlook12") #new credentials
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials() #deleting credentials account
        self.assertEqual( len(Credentials.credentials_list),1)

        
if __name__ == '__main__':
    unittest.main()
