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
     def test_save_credential(self):
       
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)  


    def tearDown(self):
            
            Credential.credential_list = []    


    def test_save_multiple_credential(self):
            
            self.new_credential.save_credential()
            test_credential = Credential("Test1","user","apple","test1@user.com") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)

    def test_delete_credential(self):
            
            self.new_credential.save_credential()
            test_credential = Credential("Test2","user","ball","test2@user.com") 
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1) 
    def test_find_credential_by_credential_name(self):
       

        self.new_credential.save_credential()
        test_credential = Credential("Test3","user","curry","test3@user.com") 
        test_credential.save_credential()

        found_credential = Credential.find_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)  

                

    