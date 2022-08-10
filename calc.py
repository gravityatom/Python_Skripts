# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import argparse
import sys
#Creation of the Parser
parser = argparse.ArgumentParser(description = 'Python Calculator: only addition, subtraction, and multiplication')

#Add the first number argument
parser.add_argument('--number1', type=int, required=True)

#Add the second number argument
parser.add_argument('--number2', type=int, required=True)

#Add the option argument
parser.add_argument('--operation', type=str, required=True, help = "Avaiable values for add, sub, multiplication: a, s, m")

#Parse the argument
try:
    args = parser.parse_args()
except:
    parser.print_help()
    sys.exit(0)

#Defining the different operations that are available to use
def add_numbers(number1, number2):
    sum = number1 + number2
    
    return sum

def subtract_numbers(number1, number2):
    diff = number1 - number2
    
    return diff

def multiplication_numbers(number1, number2):
    product = number1 * number2
    
    return product

#If-Then statements that defines which operation the user requested
if args.operation == 'a':
   sum = add_numbers(args.number1, args.number2)
   print(f"{sum}")
    
if args.operation == 's':
    diff = subtract_numbers(args.number1, args.number2)
    print(f"{diff}")

if args.operation == 'm':
    product = multiplication_numbers(args.number1, args.number2)
    print(f"{product}")

