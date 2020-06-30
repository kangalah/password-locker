import unittest
from user_credentials import Users, Credentials

class TestUsers(unittest.TestCase):
    """
    Test class that defines test cases for the Users behaviour
    """
    def setUp(self):
        self.new_user = Users("Nanjala", "Joan", "password")

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_user.first,"Nanjala")
        self.assertEqual(self.new_user.last,"Joan")
        self.assertEqual(self.new_user.password,"password")

    def test_save_user(self):
        """
        test_save_user test case to test if the object is saved
        """

        self.new_user.create_user()
        self.assertEqual(len(Users.user_info),1)

    def tearDown(self):
        """
        Function to destuct functions after set up
        """
        Users.user_info = []

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the Credentials behaviour
    """
    def test_auth_check(self):
        """This is a test to test if the user provided correct information
        """
        self.new_user = Users("Nanjala", "Joan", "password")
        self.new_user.create_user()
        another_user = Users("user2","othername","password2")
        another_user.create_user()

        for cred in Users.user_info:
            if cred.first == another_user.first and cred.password == another_user.password:
                identity = another_user.first

                return identity

    def test_setup(self): 
        self.new_cred = Credentials("Nanjala","Joan","Instagram","password") 

    def test_init(self):
        """
        test_init to check if the credentials objects are initialized correctly
        """
        self.new_cred = Credentials("Nanjala","Joan","Instagram","password")
        self.assertEqual(self.new_cred.name, "Nanjala") 
        self.assertEqual(self.new_cred.username,"Joan") 
        self.assertEqual(self.new_cred.platform,"Instagram")
        self.assertEqual(self.new_cred.password,"password")

    def test_save_cred(self):
        """
        Test to check if the object is saved to credentials_info
        """
        self.new_cred = Credentials("Nanjala","Joan","Instagram","password")
        self.new_cred.save_cred()
        self.assertEqual(len(Credentials.credentials_info),5)

    def tearDown(self):
        """
        reinitializes the credentials_info list to its empty state
        """
        Credentials.credentials_info = []

    def test_show_credentials(self):
        """
        test to check if credentials saved is displayed
        """
        self.new_cred = Credentials("Nanjala","Joan","Instagram","password")
        self.new_cred.save_cred()
        self.another_cred = Credentials("Nanjala","Joan","Instagram","passwprd")
        self.another_cred.save_cred()
        self.assertEqual(len(Credentials.show_credentials(self.new_cred.username)),1)

    def test_find_platform(self):
        """
        test to search credentials per account
        """
        self.new_cred = Credentials("Nanjala","Joan","Instagram","password")
        self.new_cred.save_cred()
        Instagram = Credentials("Nanjala","Joan","Instagram","password")
        Instagram.save_cred()
        self.assertEqual(Credentials.find_platform('Instagram'),Instagram)

    def test_del_cred(self):
        """
        test to delete credentials from the credentials list
        """
        Credentials.credentials_info = []
        self.new_cred = Credentials("Nanjala","Joan","Instagram","password")
        self.new_cred.save_cred()
        Instagram = Credentials("Nanjala","Joan","Instagram","password")
        Instagram.save_cred()
        del_item = Credentials.find_platform('Instagram')
        self.assertEqual(Credentials.del_cred(del_item),"Deleted")

if __name__ =='__main__':
    unittest.main()




