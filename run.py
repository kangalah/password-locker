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

        if user_input =='cu':
            print("You have selected to register.Please enter your registration details below")
            fname = input("Enter your first name: ")
            lname = input("Enter your last name: ")
            password = input("Enter your desired password: ")
            register_user(create_user(fname, lname, password))
            print(f"Your account is registered as follows: First name:{fname}Last name:{lname}password:{password}is your password")

        elif user_input == 'li':
            print("Enter your first name and password to log in to your account\n")
            username = input("Enter your username here: ")
            password = input("Enter your password here: ")
            if user_check(username,password == username;
            print(f"Welcome{username}. Your login was successful")

            while True:
                print("********")
                print("please use the following hort codes to use the password vault")
                user_input = input("cc - save new credentials\n ccp - Create new credentials with generated pasword\n dc - display credentials\n del - Delete credentials\n ex - Exit")


        if user_input == 'cc':
            print("Enter the account details that you want to save below")
            username = input("Enter your username: ")
            platform = input("Enter your platform: ")
            password = input("Enter your password: ")
            create_cred(fname,username,platform,password)
            print(f"Your credentials for site: {platform}, with {username} and password:{password} has been saved!")

            elif user_input == 'ccp':
                print("Enter the account details you want saved below")
                username = input("Enter your username: ")
                platform = input("Enter the platform: ")
                len = input("Enter the length of your desired password(Numbers only): ")
                password = password_gen(int(len))
                create_cred(fname,username,platform,password)
                print(f"Your credentials for account: {platform}, with username: {uername} and password:{password} have been saved!")

                elif user_input == 'dc':
                    print("Your saved credentials are as below")
                    show_cred(username)

                elif user_input == 'del':
                    print("Enter the account name and username whose credentials you want to delete below")
                    platform = input("Enter the name of the account here e.g instagram: ")
                    username = input("Enter your username here: ")
                    show_cred(username)
                    print("Your credentials have been deleted successfully!")

                if user_input == 'ex':
                    print(Goodbye {username}!)
                    break
                elif user_input == 'lo'
                print("Thank you for using the password-locker")
                break

            else:
                print("Wrong Input! kindly choose again")

if __name__ == '__main__':
    main()


