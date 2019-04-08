#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_user(login_name,password):
    '''
    Function to create a new  user
    '''
    new_user = User(login_name,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def create_credentials:
    '''
    Function to create a new redential
    '''
    new_credentials = Credentials(platform,name,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credentials
    '''
    credentials.delete_credentials()


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello! Welcome to your personal password locker. What is your name?")
    login_name = input()

    print (f"Hello {login_name}. What would you like to do?")
    print('\n')

    while True:
        print(" Please Use these short codes to navigate: \n na - create a new Account, li - log into your account, ex = exit the password locker app ")
            
        short_code = input().lower()

        if short_code == 'na':
            print("New Account")
            print("-"*10)   

            print("login name.....")
            first_name = input()

            print("Password....")
            password = input()

            save_user (create_new_user(first_name, last_name, user_name, password))  
            print('\n')
            print(f"New Account for {login_name } created")
            print (f'hello {login_name}, you are now logged in!')
            print('\n')
            while True:
                    print('To proceed use these shortcodes:\n cc - Create new Credentials, dc - Delete Credential, fd - Find Credential, ds - display saved credentials, ex - exit')
                    short_code = input().lower()
                    if short_code == 'ex':
                        print ('\n')
                        print(f'Goodbye { login_name}.')
                        break

                    if display_credentials():
                            print ('\n')
                            print('Here is a list of your saved credentials')
                            print('\n')

                            for credential in display_credentials():
                                print(f'Platform: { credential.account_platform}')
                                print(f'Account Name: {credential.account_name}')
                                print(f'Account Password: {credential.account_password}')
                                print('\n')
                        else:
                            print ('\n')
                            print ('Looks like you haven\'t saved that credential yet!')
                            print ('\n')
                    elif short_code == 'cc':
                        print ('\n')
                        print ("New Credentials")
                        print ("-"*10)

                        print("Acount platform:")
                        account_platform = input()

                        print("Account name:")
                        account_name = input()

                        while True:
                            print('Please choose an option for entering your password by choosing a short-code! \n mp -enter my password, gp - generate a password for me!')
                            short_code = input().lower()
                            if short_code == 'mp':
                                print("Account password:")
                                account_password = input()
                                break
                            elif short_code =='gp':
                                chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                                account_password = "".join(random.choice(chars) for _ in range(10))
                                break
                            else: 
                                print('Ooops!I did not get that. Please try again!')
                            

                        save_credentials(create_credentials(account_platform, account_name, account_password))
                        print('\n')
                        print(f'New Credentials: {account_platform } {account__name } {account_password}')
                        print('\n')
     

        elif short_code =='ex':
            print("Have a lovely day!")
            break
        else:
            print('\n')
            print("I really didn't get that. Please use the short codes")
            print('\n')

if __name__ == '__main__':
     main()
                         