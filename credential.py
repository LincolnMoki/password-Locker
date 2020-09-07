class Credential:
    """
    Class that generates new instances of users.
    """
    credential_list = []

    def __init__(self,credential_name,usr_name,password,email):
        self.credential_name = credential_name
        self.usr_name = usr_name
        self.password = password
        self.email = email

    def save_credential(self):

      

        Credential.credential_list.append(self)    

