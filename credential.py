class Credentials:
    """
    Class that generates new instances of credentials.
    """ 

    credentials_list = []

    def __init__(self,account_platform, account_name, account_password):
        self.account_platform = account_platform
        self.account_name = account_name
        self.account_password = account_password

   


