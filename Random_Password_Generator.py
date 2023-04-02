# Creating a random password generator in Python

# Step 1: Import necessary Python libraries
import secrets
import string

# Step 2: Define all character possibilities (letters, digits, special characters)
letters = string.ascii_letters # ascii_letters is the concatenation of all upper and lowercase letters
digits = string.digits # digits is a string containing numbers 0 to 9
special_chars = string.punctuation # punctuation is a string of all special characters

# Step 3: Concatenate the 3 strings from step 2 and store them in a variable
characters = letters + digits + special_chars

# Step 4: Store the desired length of the password in a variable
password_length = 12

# Step 5: Generate a password string
password = ''
for i in range(password_length):
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

