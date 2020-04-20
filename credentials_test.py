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
        self.new_credentials = credentials("pete","gmail","yahoo","gmail08")

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
        self.assertEqual( self.new_credentials.Credentials_email, "yahoo")
        self.assertEqual( self.new_credentials.credentials.credentials_password, "gmail08")

    def test_save_credentials(self):
        """
        test to see whether user is saved to user list
        """
        
        self.new_credentials.test_save_credentials()

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

        test_credentials = Credentials("john", "outlook","yahoo", "outlook12")

        test_credentials.save_credentials()

        test_credentials = Credentials("john", "glassdoor","yahoo","glassy05")

        test_credentials.save_credentials()

        self.assertEqual( len(Credentials.display_credentials("john")), 2)

    def test_credentials_exist(self):
        """
        Test to check if we can return boolean for credentials not found
        """

        self.new_credentials.save_credentials()

        test_credentials = Credentials("john","outlook","yahoo","outlook12") # new credentials

        test_credentials.save_credentials()

        # with use of contact exist method
        credentials_exists = Credentials.credentials_exists("outlook")

        self.assertTrue(credentials_exists)

    # deleting a credentials account
    def test_delete_credentials():
        """
        this method enables user to remove credentils the he/she no longer needs
        """

        self.new_credentials.save_credentials()
        test_credentials = Credentials("john","outlook","yahoo","outlook12") #new credentials
        test_credentials.save_credentials

        self.new_credentials.delete_credentials() #deleting credentials account
        self.assertEqual( len(Credentials.credentials_list,),1)

    #pyperclip function to copy email
    def test_copy_credentials_email():
        """
        function that copy email address from a found credentials
        """
        return Credentials.copy_credentials_email()

    # main function
    def main():
        """
        Function to run the password locker app
        """

        print("Hello Welcome to your passwordlocker \n use this short codes to get around")

        while True:
            """
            loop that is running the entire epplication 
            """
                    print ("""Short codes:
                    cu - create a password Locker account \n
                    du - display names of current password locker users \n
                    lg - log into your account on password locker \n
                    dlc - delete a password locker account you no longer need \n
                    ex - exit the password locker account """)

                    # taking short codes from the user
                    short_code = input().lower()

                    if short_code == "cu":
                        
                        print("\n")
                        print(" New password locker account")
                        print ("-"*10)

                        print("User name ...")
                        user_name = input()

                        print("password ...")
                        user_password = input()

                        #creating a new user and saving
                        save_users( create_user( user_name, user_password))

                        print("\n")
                        print(f"Welcome {user_name} to Password Locker")

                    elif short short_code == "du":
                        """
                        show names of present user
                        """
                        if display_users():
                            print("\n")
                            print("Below ere the current user of password locker")
                            print(print"-"*10)

                            for user in disp


                    elif short_code == "lg":
                        """
                        code to allow user log into password locker
                        """
                        print("\n")
                        print("Log into your Password Locker Account")
                        print("Enter the user name")
                        user_name = input()

                        print("Enter the password")
                        user_password = input()

                        if user_log_in( user_name,user_password) == None:
                            print("\n")
                            print("invalid user name or password, try again or create a new account")
                            print("\n")

                        else:

                            user_log_in(user_name,user_password)
                            print("\n")
                            print(f""" {user_name} You have successfully loged to you =r credentials \n 
                            use the following short codes to navigate""")

                            while True:
                                """
                                loop for running functions post log-in
                                """
                                print(""" Short codes:
                                cc - add a credential  """)

    


    if __name__ == '__main__':
        unittest.main(verbosity=2)
