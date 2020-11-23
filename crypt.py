import os
from cryptography.fernet import Fernet


def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from file `key.key`
    """
    return open("key.key", "rb").read()


def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)


def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    """
    A simple interface for user based on switch/cases 
    """
    option = input("Chose what you want to do: "\
            "\n\n1.Generate key\n2.Encrypt file\n3.Decrypt file\n\n"\
            "Your choise: ") 
    file = ""
    key = ""

    if option == "1":
        write_key()
        key = load_key()
        print("Your secret key: " + str(key)[2:-1])
        

    elif option == "2":
        while len(file) == 0:
            file = input("File to encrypt (like data.txt)") 

        sub_option = input("Chose what you want to do: "\
                    "\n\n1.Get generated key from file\n2.Generate new key and use it "\
                    "\n3.Use my key\n\nYour choise: ") 
        
        if sub_option == "1":
            write_key()
            key = load_key()
                        
        elif sub_option == "2":
            key = load_key()
            print("Your secret key: " + str(key)[2:-1])
            
        elif sub_option == "3":
            while len(key) == 0:
                key = input("Your key:")

        encrypt(file, key)
                
    elif option == "3":
        while len(file) == 0:
            file = input("File to decrypt (like data.txt): ") 
            
        sub_option = input("Chose what you want to do: "\
                    "\n\n1.Get generated key from file\n2.Use my key\n\n"\
                    "Your choise: ") 
        
        key = load_key()

        if sub_option == "1":
            key = load_key()
            
        elif sub_option == "2":
            while len(key) == 0:
                key = input("Your key: ")

        decrypt(file, key)

