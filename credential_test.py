import unittest # Importing the unittest module
from credential import Credential # Importing the credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credential("Twitter","Chiri","pass123") # create credential object
    
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credential.account_platform,"Twitter")
        self.assertEqual(self.new_contact.account_name,"Chiri")
        self.assertEqual(self.new_contact.account_password,"pass123")

if __name__ == '__main__':
    unittest.main()    
