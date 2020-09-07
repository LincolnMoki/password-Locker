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