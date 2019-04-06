import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Twitter","Chiri","pass123") # create credential object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.account_platform,"Twitter")
        self.assertEqual(self.new_credentials.account_name,"Chiri")
        self.assertEqual(self.new_credentials.account_password,"pass123")

if __name__ == '__main__':
    unittest.main()    
