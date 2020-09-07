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
     
               