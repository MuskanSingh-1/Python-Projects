import string
import random

#Funtion for generating a single password
def password_gen(length):

    #Generates a random password of specified length.
    #Parameters:length (int): Length of the password

    if length < 8:
        raise ValueError("Password length should be at least 8 characters")
    
    # Define character sets
    digits = string.digits
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation

    # Ensure the password includes at least one character from each set
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the remaining length of the password
    password += random.choices(all_characters, k=length-4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    return ''.join(password)

#Funtion to generate multiple passwords of specified length
def multiple_passwords(number_of_passwords, length):
    #Generates a specified number of random passwords.
    '''Parameters:number_of_passwords (int): Number of passwords to generate
               length (int): Length of each password'''

    return [password_gen(length) for _ in range(number_of_passwords)]

#Main funtion for the user interface and for calling the above two funtions to generate password
def main():
    print("Welcome to the Secure Password Generator!")
    print("Please follow the instructions to generate your secure passwords.")
    
    try:
        number_of_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the length of each password: "))
        
        passwords = multiple_passwords(number_of_passwords, length)
        
        print("\nYour secure passwords are: ")
        for i, password in enumerate(passwords, 1):
            print(f"{i}: {password}")
    except ValueError as e:
        print(f"Error: {e}. Please enter valid numbers.")

if __name__ == "__main__":
    main()