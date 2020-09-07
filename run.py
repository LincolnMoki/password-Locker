from user import User
from credential import Credential

def create_user(account_name,user_name,password,email):
   
    new_user = User(account_name,user_name,password,email)
    return new_user

def save_user(user):
    
    user.save_user()    

def del_user(user):
    
    user.delete_user()    
	
def find_user(name):
    
    return User.find_by_user_name(name)    

def check_existing_user(name):
    
    return User.user_exist(name)    

def display_user():
    
    return User.display_user_name() 
def create_credential(credential_name,usr_name,password,email):
    
    new_credential = Credential(credential_name,usr_name,password,email)
    return new_credential

def save_credential(credential):
   
    credential.save_credential()    

def del_credential(credential):
   
    credential.delete_credential()    


def find_credential(name):
    
    return Credential.find_by_name(name)    

def check_existing_credential(name):
   
    return Credential.credential_exist(name)    

def display_credential():  
    
    return Credential.display_credential() 

def main():
    print("Hello and Welcome to Password locker. What is your name?")
    user_name = input()
    print(f"Hello {user_name}, sign up to create an account.")
    print('\n')
    while True:
        print("Use these known short codes to operate :\n su -> SIGN UP.\n vw -> view your account.\n lg ->LOGIN.\n ex ->exit . ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Pass Word Locker Account")
            print("_"*100)
            account_name = input('Account name:')
            print ('\n')
            u_name = input('User name:')
            print ('\n')
            pwd = input('Password : ')
            print ('\n')
            e_address = input('Email address:')
            save_user(create_user(account_name,user_name,pwd,e_address)) 
            print ('\n')
            print(f"A New {account_name} Account with the user name  {u_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')