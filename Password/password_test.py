import pyperclip
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
        '''
        test_init test case to test if the object is initialized properly 
        '''
        self.assertEqual(self.new_password.first_name,"Duncan")
        self.assertEqual(self.new_password.last_name,"Arani")
        self.assertEqual(self.new_password.security,"")
        self.assertEqual(self.new_password.email,"duncanarani@gmail.com")


def test_save_contact(self):
        
        # test_save_password test case to test if the password object is saved into
        #  the password list
        
        self.new_password.save_password() # saving 
        self.assertEqual(len(Password.password_list),1)


def tearDown(self):
        # tearDown method that does clean up after each test case has run.
        Password.password_list = []

# other test cases here
def test_save_multiple_password(self):
        
        # test_save_multiple_password to check if we can save multiple password
        # objects to our password_list
    
        self.new_password.save_password()
        test_password = Password("Test","first_name","last_name","email","password") # new contact
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)

def delete_pssword(self):

        # deletes a saved password from the password_list

        Password.password_list.remove(self)


        #  Decorators allow you to make simple modifications to callable objects like functions, methods, or classes.



@classmethod
def find_by_emails(classes,name):
    
     
     for password in classes.password_list:
            if password.email == name:
                return Password

#  loops through all the saved password and checks if any matches the emails
@classmethod
def password_exist(classes,name):
        
        for password in classes.password_list:
            if password.email == name:
                    return True

        return False  

@classmethod
def display_password(clas):
        '''
        method that returns the contact list
        '''
        return clas.password_list

@classmethod
def copy_email(clas,name):
        password_found = Password.find_by_email(name)
        pyperclip.copy(password_found.email)

if __name__ == '__main__':
    unittest.main()
