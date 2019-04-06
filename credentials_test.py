import unittest # Importing the unittest module
from credentials import Credentials # Importing the credentials class

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credential_list = []


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

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into
         the credentials list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credentials_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Account","Name","pass222") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),3)

    def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a credentials from our credentials list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test","Account","name","pass222") # new credentials
            test_credentials.save_credentials()

            self.new_credentials.delete_credentials()# Deleting a credentials object
            self.assertEqual(len(Credentials.credentials_list),1)

      def test_find_credential_by_name(self):
            '''
            test to check if we can find credentials and display information"""
            '''
            self.new_credentials.save_credentials()
            new_test_credential = Credentials("Twitter", "56789")
            new_test_credential.save_credentials()

            found_credential = Credentials.find_by_name("Twitter")

            self.assertEqual(found_credential.account_name, new_test_credential.account_name)
    
   
if __name__ == '__main__':
    unittest.main()    
