#!/usr/bin/python3

import argparse
import sys
import string
import random
#creation of the parser
parser = argparse.ArgumentParser(description = 'password generator')

#add an argument
parser.add_argument('--length', type = int,  default = 8, help = \
"password length. default length is set at 8")

#parse the arguments
args = parser.parse_args()

#setting variable values
uppercaseletter1 = random.choice(string.ascii_uppercase)

uppercaseletter2 = random.choice(string.ascii_uppercase)

lowercaseletter1 = random.choice(string.ascii_lowercase)

lowercaseletter2 = random.choice(string.ascii_lowercase)

digit1           = random.choice(string.digits)

digit2           = random.choice(string.digits)

symbol1          = random.choice(string.punctuation)

symbol2          = random.choice(string.punctuation)

#concatening the characters to make password
password         = uppercaseletter1 + uppercaseletter2 + \
lowercaseletter1 + lowercaseletter2 + digit1 + digit2 + symbol1 + symbol2

#converting the password into a list
password_list    = list(password)

#shuffling the password characters
random.shuffle(password_list)
new_password     = "".join(password_list)

#if-then statement to determine the length of the password
if (len(new_password) < args.length):
    char_diff    = args.length - len(new_password)
    avail_chars  = string.ascii_letters + string.digits + \
    string.punctuation

    new_pw_chars = "".join(random.choices(avail_chars, k = char_diff))

    new_password = new_password + new_pw_chars

print(f"new_password: {new_password}")
