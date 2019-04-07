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

    def delete_credentials(self):

        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)

    def test_find_credentials_by_account(self):
        '''
        test to check if we can find a contact by phone number and display information
        '''

     
