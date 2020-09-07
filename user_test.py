import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):	
    
     def setUp(self):
         
         
          self.new_user = User("Alpha","Rome","rome231")
          
          
          
     def test_init(self):
          
        self.assertEqual(self.new_user.first_name,"Alpha")
        self.assertEqual(self.new_user.last_name,"Rome")
        self.assertEqual(self.new_user.password,"rome231")
        
     def test_save_user(self):
       
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1)
        
     def test_save_multiple_user(self):
       
        self.new_user.save_user()
        test_user = User("Facebook","Alpha","Rome","rome231") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
    
               