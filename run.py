#!/usr/bin/env python3.7
"""
Run module 

File that runs the application
import the two class modules to be run
"""

from user import User
from credentials import Credentials

def create_user(name, password):
    """
    function that creates a user account

    Args
        name: name of choice by user for their account
        password: select password that user wants for their account
    """

    new_user = User(name, password) 

    return new_user

def save_users(user):
    """
    Function to save the user account created

    Args
        user: the user account to be saved 
    """

    user.save_user()

def check_existing_users(name):
    '''
    Function that checks if a user account name already exists

    Args:
        name : the user account name
    '''

    return User.user_exist(name)

def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account

    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)

def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()

def create_credentail(user_password, name, password):
    '''
    Function to create a credential 

    Args:
        user_password : the password for Password Locker
        name : the name of the account 
        password : the password for the account
    '''

    new_credentail = Credential(user_password,name,password)

    return new_credentail

def save_credentials(credentials):
    '''
    Function to save a credentials

    Args:
        credentials : the credentials to be saved
    '''

    credentials.save_credentials()

def check_existing_credentials(name):
    '''
    Function that checks if a user credentials name already exists

    Args:
        name : the credentials name
    '''

    return Credentials.credentials_exist(name)

def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credential.display_credential(password)

def create_generated_password(name):
    '''
    Function that generates a password for the user 

    Args:
        name : the name of the account
    '''
    password = Credentials.generate_password()

    return password

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
            print(f"Welcome {user_name} to Password Locker 😇")

        elif short_code == "du":
            """
            show names of present user
            """
            if display_users():
                print("\n")
                print("Below ere the current user of password locker")
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print("\n")
                print("password locker does not have a user yet. \n  Be the first user 🎉 ")
                print("\n")


        elif short_code == "lg":
            """
            code to allow user log into password locker
            """
            print("\n")
            print("Log into your Password Locker Account 🎨")
            print("Enter the user name")
            user_name = input()

            print("Enter the password")
            user_password = input()

            if user_log_in( user_name,user_password) == None:
                print("\n")
                print("🚫 invalid user name or password, try again or create a new account")
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
                    cc - add credentials  \n
                    dc - display credentials \n
                    gc - generate a credentials with autogenerate password \n
                    ce - copy email of existing credentials \n
                    dlc - delete credentials \n
                    ext - exit credentials """)


                    # get short codes from user

                    if short_code == "cc":
                        print("\n")
                        print("New Credentials")
                        print("-"*10)

                        print("Name of the credentials ...")
                        credentials_name = input()

                        print("Email link of the credentials ...")
                        Credentials_email = input()

                        print("Password of the credentials ...")
                        credentials_password = input()
    
                        # creating and saving a new user
                        save_credentials ( create_credentials(user_password, credentials_name, Credentials_email, credentials_password))

                        print("\n")
                        print(f"Credentials for {credentials_name} have been recorded and saved 🏆")
                        print("\n")

                    elif short_code == "dc":
                        """
                        displaying credential name & password
                        """
                        if display_credentials(user_password):
                            print("\n")
                            print(f"{user_name}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(user_password):
                                print(f"Account ..... {credentials.credentials_name}")
                                print(f"Password .... {credentials.credentials_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("Sorry You do not have any credentials 😟 ")
                            print("\n")

                    elif short_code == "gc":
                        """
                        creating a credentials with autogenerated password
                        """
                        print("\n")
                        print("New Credentials")
                        print("-"*10)

                        print("Name of the credentials ...")
                        credentials_name = input()

                        # Save created credential with its generated password
                        save_credentials( Credentials(user_password, credentials_name, Credentials_email, (create_generated_password(credentials_name)) ) )
                        print("\n")
                        print(f"Credentials for {credentials_name} have been created and saved 📁")
                        print("\n")

                    elif short_code == "ce":
                        print("Enter credentials email you wish to copy")

                        copy_credentials_email = input()
                        if check_credentials_exists(copy_credentials_email):
                            copy_credentials_email = find_credentials(copy_credentials_email)
                            print(f"{copy_credentials_email.Credentials_email}")
                            print(f"{Credentials_email} has been copied 📋")

                    elif short_code == "dlc":
                        """
                        deleting credentials that are no longer needed
                        """
                        print("enter name of credentials you no longer need")

                        delete_credentials = input()
                        if check_credentials_exists(delete_credentials):
                            delete_credentials = find_credentials(delete_credentials)
                            print(f"{delete_credentials.user_name} {delete_credentials.user_password}")
                            print(f"The credentials {user_name} {credentials_name} has been deleted 🚮")


                    elif short_code == "ext":
                        print(f"Thank you {user_name} for using password locker. see you soon 👋")
                        print("\n")
                        break

                    else:
                        print("\n")
                        print(f""" {short_code} seems to be incorrect 😬. \n 
                        please use the short codes provided""")
                        print("\n")
        elif short_code == "ex":
            """
            Exiting password locker
            """
            print("\n")
            print("Bye, have a good day 🚀.....")

            break

        else:
            print("\n")
            print(f""" Invalid entry please check amd try again. what is the the {short_code}? 
            please use the short codes """)
            print("\n")

if __name__ == '__main__':
    main()