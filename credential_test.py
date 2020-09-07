import unittest 
from credential import Credential


class TestCredential(unittest.TestCase):
    def setUp(self):
       
        self.new_credential = Credential("Alpha","Rome","231","Alpharome@gmail.com") 
    
    def test_init(self):
        

        self.assertEqual(self.new_credential.credential_name,"Alpha")
        self.assertEqual(self.new_credential.usr_name,"Rome")
        self.assertEqual(self.new_credential.password,"231")
        self.assertEqual(self.new_credential.email,"Aplharome@gmail.com")