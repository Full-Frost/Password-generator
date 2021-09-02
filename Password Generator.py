import string
import random
import sys
import os
import pprint

password_library = {}

def manage_word_of_pass():
    while True:
        ans = input("Would you like to add a password to the save file? [y/n]")
        if ans =='y':
            name = input("What would you like to name the password?")
            passw = input("What is the password you would to add to the file?")
            password_library[name] = passw
        else:
            word = input("Ok would you like to generate a password? [y/n]")
            if word == 'y':
                print("please use numbers 1-3, 1 is the weakest option while 3 is the strongest")
                generate_word_of_pass()
            else:
                end = input("Would you like to store your passwords locally? [y/n]")
                if end == 'y':
                    file_maker()
                else:
                    print("Have a nice day.")
                    sys.exit()


def generate_word_of_pass():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    letters = string.ascii_letters
    nums = string.digits
    puncs = string.punctuation
    password = []
    while True:
        strength = input("Please enter desired password strength: ")
        if strength == '1':
            password.append(''.join(random.choice(letters) for i in range(random.randint(4, 6))))
            password.append(''.join(random.choice(lower) for i in range(random.randint(4, 6))))
            password.append(''.join(random.choice(puncs) for i in range(random.randint(2, 4))))
            password.append(''.join(random.choice(nums) for i in range(random.randint(2, 4))))
        elif strength == '2':
            password.append(''.join(random.choice(letters) for i in range(random.randint(6, 8))))
            password.append(''.join(random.choice(puncs) for i in range(random.randint(3, 5))))
            password.append(''.join(random.choice(upper) for i in range(random.randint(1, 3))))
            password.append(''.join(random.choice(lower) for i in range(random.randint(2, 4))))
            password.append(''.join(random.choice(upper) for i in range(random.randint(1, 3))))
            password.append(''.join(random.choice(nums) for i in range(random.randint(3, 5))))
            password.append(''.join(random.choice(letters) for i in range(random.randint(4, 6))))
        elif strength == '3':
            password.append(''.join(random.choice(letters) for i in range(random.randint(2, 5))))
            password.append(''.join(random.choice(puncs) for i in range(random.randint(2, 5))))
            password.append(''.join(random.choice(upper) for i in range(random.randint(3, 6))))
            password.append(''.join(random.choice(lower) for i in range(random.randint(2, 5))))
            password.append(''.join(random.choice(letters) for i in range(random.randint(2, 5))))
            password.append(''.join(random.choice(nums) for i in range(random.randint(4, 7))))
            password.append(''.join(random.choice(puncs) for i in range(random.randint(3, 6))))
            password.append(''.join(random.choice(letters) for i in range(random.randint(4, 7))))
            password.append(''.join(random.choice(nums) for i in range(random.randint(2, 5))))
        else:
            print("invalid input please try again")
            break
        joined = ''.join(password)
        print(joined)
        while True:
            save = input("Would you like to save the password? [y/n]")
            if save == 'y':
                name = input("What would you like to name the password? ")
                password_library[name] = joined
                while True:
                    display = input("Would you like to display the password? [y/n]")
                    if display == 'y':
                        print(password_library)
                    else:
                        print("Ok")
                        break
            elif save == 'n':
                print("Ok")
                break
            else:
                print("invalid input")
                break
        while True:
            cont = input("Would you like a new password? [y/n]")
            if cont == 'y':
                break
            elif cont == 'n':
                end = input("Would you like to store your passwords locally? [y/n]")
                if end == 'y':
                    file_maker()
                else:
                    print("Have a nice day. ")
                    sys.exit()

def file_maker():
    create = input("Would you like to create a file to store your passwords? [c/s]")
    if create == 'c':
        name = input("what would you like the file name to be? ")
        file = open(name, "w+")
        file.write(pprint.pformat(password_library))
        #file.write(password_library.keys())
        #file.open("Password.txt", "r")
        #file.close()
    else:
        add = input("Would you like to add your password to an already existing txt file? [y/n]")
        if add == 'y':
            path = input("What is the file path to the file?")
            name = input("What is the exact name of the file?")
            find_file(name, path)
            file = open(name, "a+")
            file.write(pprint.pformat(password_library))
            #file.close()
        else:
            print("Have a good day.")
            sys.exit()

def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def main():
    manage_word_of_pass()

main()
