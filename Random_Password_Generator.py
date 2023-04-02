# Creating a random password generator in Python

# Step 1: Import necessary Python libraries
import secrets # Used the secrets library rather than the random library to generate cryptographically secure passwords
import string # Used the strings library to generate all character possibilities by type rather than individually typing them 

# Step 2: Define all character possibilities (letters, digits, special characters)
letters = string.ascii_letters # ascii_letters is the concatenation of all upper and lowercase letters
digits = string.digits # digits is a string containing numbers 0 to 9
special_chars = string.punctuation # punctuation is a string of all special characters

# Step 3: Concatenate the 3 strings from step 2 and store them in a variable
characters = letters + digits + special_chars

# Step 4: Store the desired length of the password in a variable (Secure passwords are long to decrease predictability 
password_length = 12

# Step 5: Generate a password string
password = ''
for i in range(password_length): # Used a for loop to repeat sampling of random characters
    password += ''.join(secrets.choice(characters))

# Step 6: Generate a password given constraints
while True:
    password = ''
    for i in range(password_length):
        password += ''.join(secrets.choice(characters))

    if (any(char in special_chars for char in password) and 
        sum(char in digits for char in password)>=2):
            break
print("Your random password is: ", password)

