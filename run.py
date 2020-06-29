#!/usr/bin/env python3.8
from user_credentials import Users, Credentials

def create_user(first,last,password):
    '''
    Creates a new user account
    '''
    user_new = Users(first,last,password)
    return user_new

def register_user(user):
    '''
    saves the created user's account
    '''
    Users.create_user(user)

def user_check(first,password):
    '''
    checks whether user exists before creating any new credentials
    '''
    return Credentials.user_check(first,password)

def create_cred(name,username,platform,password):
    '''
    Creates credentials to be saved
    '''
    create_instance = Credentials(name,username,platform,password)
    return create_instance

def save_cred(cred):
    '''
    saves created user credentials
    '''

def password_gen(size):
    '''
    generates a random password_gen
    '''
    random = Credentials.password_gen(size)
    return random

def show_cred(username):
    '''
    Displays saved credentials
    '''
    return Credentials.show_credentials(username)


def main():
    print("welcome to Nanjala password Locker app")
    while True:
        print("**********i")
        print("Please use the following short codes to interact with this application app\n li - Login\n cu - Register\n lo - Logout")
        user_input = input("Enter input here: ")

        if user_input == 'cu'
        print("You have selected to register.Please enter your registration details below")
        fname = input("Enter your first name: ")
        lname = input("Enter your last name: ")
        password = input("Enter your desired password: ")
        register_user(create_user(fname, lname, password))
        print(f"Your account is registered as follows: First name:{fname}Last name:{lname}password:{password}is your password")


        elif user_input == 'li':
            print("Enter your first name and password to log in to your account\n")

