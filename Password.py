import string
import random
Alphabit = list(string.ascii_uppercase)
Alphabit_Lower = list(string.ascii_lowercase)
Digits = list(string.digits)
Punctution = list(string.punctuation)

characters_number = int(input("Enter How many characters u want in ur password."))

random.shuffle(Alphabit)
random.shuffle(Alphabit_Lower)
random.shuffle(Digits)
random.shuffle(Punctution)

#Parts of the password 

first_part = (characters_number * 30/100)
second_part = (characters_number * 20/100)

