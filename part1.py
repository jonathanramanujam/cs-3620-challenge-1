# Jonathan Ramanujam
# CS 3620
# Python Basics
# Part 1: Calculating Simple Interest

from lib2to3.pgen2.token import NEWLINE
from tokenize import String


def SimpleInterest(principal, number_of_years, rate_of_interest):
    return (principal * number_of_years * rate_of_interest)/100

def StringToInt(string):
    return int(float(string))

print("\nLets calculate simple interest!")
principal = input("Please enter the principal: ")
number_of_years = input("Please enter the number of years: ")
rate_of_interest = input("Please enter the rate of interest: ")

print(f"\nPrincipal as int: {StringToInt(principal)}")
print(f"Number of Years as int: {StringToInt(number_of_years)}")
print(f"Rate of Interest as int: {StringToInt(rate_of_interest)}")

print("\nSimple Interest: ")
print(SimpleInterest(
        StringToInt(principal),
        StringToInt(number_of_years),
        StringToInt(rate_of_interest)))
