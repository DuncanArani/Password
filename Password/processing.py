#!/usr/bin/env python3.6
from password import Password
def create_password(first_name,last_name,email,password):
    
# to create a new password

    new_password = Password(first_name,last_name,email,password)
    return new_password



def save_passwords(password):
    
    password.save_password()

def del_passwords(password):
    
    password.delete_password()


def find_password(name):
    
    return Password.find_by_names(name)


def check_existing_passwords(name):
    
    return Password.password_exist(name)



def display_password():

    return Password.display_passwords()



def main():
    print("Hello Welcome to your password list. What is your email?")
    user_name = input()

    print(f"Hello {your_email}. what would you like to access?")
    print('\n')

while True:
        print("Use these short codes : cp - create a new password, dp - display passwords, fp -find a password, ex -exit the password list ")

        short_code = input().lower()

        if short_code == 'cp':
                print("New Password")
                print("-"*10)

                print ("First name ")
                f_name = input()

                print("Last name")
                l_name = input()

                print("email")
                p_number = input()

                print("password ...")
                e_address = input()

                save_password(create_password(first_name,last_name,email,password)) 
                print ('\n')
                print(f"New Password {first_name} {last_name} {email} created")
                print ('\n')

        elif short_code == 'dp':

                if display_passwords():
                    print("Here is a list of  your saved passwords")
                    print('\n')
                
                for password in display_passwords():
                    print(f"{password.first_name} {password.last_name}{password.email}")
                    print('\n')
                    
                else:
                    print('\n')
                    print("You  have no passwords saved yet")
                    print('\n')

                                
        elif short_code == 'fp':

            print("Enter the email you want to search password for")

            search_name = input()

            if check_existing_password(search_name):

                search_name = find_password(search_name)
                print(f"{search_password.first_name} {search_password.last_name}")
                print('-' * 20)

                print(f"email{search_password.email}")
                print(f"password{search_password.password}")
            else:
                        print("That password does not exist")

                
        elif short_code == "ex":
                print("thank you")
                break

        else:
                    print("Results not found. Please use the short codes")


    
    
if__name__ == '__main__'
main() 