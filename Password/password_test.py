import unittest 
from password import Password

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("Duncan","Arani","password","duncanarani@gmail.com") # create contact object

def test_init(self):

        # test_init test case to test if the object is initialized properly 

        self.assertEqual(self.new_password.first_name,"Duncan")
        self.assertEqual(self.new_password.last_name,"Arani")
        self.assertEqual(self.new_password.security,"")
        self.assertEqual(self.new_password.email,"duncanarani@gmail.com")


def test_save_password(self):
        
        self.new_password.save_password() # saving the new password
        self.assertEqual(len(Password.password_list),1)

def test_save_multiple_password(self):
            
        
            self.new_password.save_password()
            test_password = Password("Test","user","email","password") 
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)

def delete_password(self):


        Password.password_list.remove(self)



if __name__ == '__main__':
    unittest.main()
