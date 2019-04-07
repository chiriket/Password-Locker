class Credentials:
    """
    Class that generates new instances of credentials.
    """ 

    credentials_list = []

    def __init__(self,account_platform, account_name, account_password):
        self.account_platform = account_platform
        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):

        '''
        save_credentials method saves credentials objects into credential_list
        '''

        Credentials.credentials_list.append(self)

    def create_credentials(self):

        '''
        create_credentials method adds credentials objects into credential_list
        '''

        Credentials.credentials_list.append(self)

    

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)


    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list

 
     
