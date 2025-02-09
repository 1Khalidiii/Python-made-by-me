# Variables ✨

Num1 = int(input("Enter the first Number "))
Num2 = int(input("Enter the second Number "))
sign = input("Enter the mathematical operation you want to do ")

# Code ✨

#  Functions ✨

def Adding():
    Result = Num1 + Num2 
    print(Result)

def Subtracting():
    Result = Num1 - Num2 

def Multiplying():
    Result = Num1 * Num2

def Calculator():
    if sign == "+":
        Adding()
    elif sign == "-":
        Subtracting()