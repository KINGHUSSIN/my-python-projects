from math import *
import os 
import time

print("do you want to exit or not:")
print("please answer with only 'yes' or 'no'")
the_answer = input("your answer is: ")

while True and the_answer != "yes":
    print("\n\nHello!this is my first project \nso tell me if you find something wrong or if you have a idea you want me to add in, and thanks for the reviwe")
    print("if you want basic math (+ | / | * | -) please enter the word \"basic\"")
    print("and if you want to square exponent the number enter \"pow\"")
    print("and if you want to take the square root please enter \"sqrt\"")
    print("\nif you are done and want to exit enter 'exit'")
    the_choose = input("please enter what the mode do you want: ")
    if the_choose == "basic":
        num1 = input("please enter the first number: ")
        num2 = input("please enter the second number: ")
        op = input("please enter the opration mark: ")
        while True:
            try:
                num1 = float(num1)
                num2 = float(num2)
                if op == "+":
                    result = num1 + num2
                    print(result)
                    break
                elif op == "*":
                    result = num1 * num2
                    print(result)
                    break
                elif op == "/":
                    result = num1 / num2
                    print(result)
                    break
                elif op == "-":
                    result = num1 - num2
                    print(result)
                    break
                else:
                    print("invlid oprater")
                    op = input("please enter the oprator mark again: ")
            except:
                print("you need to but only numbers")
                num1 = input("please enter the first number again: ")
                num2 = input("please enter the second number again: ")

    elif the_choose == "pow":
        num1 = input("please enter the basic number: ")
        num2 = input("please enter the pow number: ")
        while True:
            try:
                num1 = float(num1)
                num2 = float(num2)
                result = pow(num1, num2)
                print(result)
                break
            except ValueError as err:
                print("please enter a number only")
                print(err)
                print("please enter the numbers again")
                num1 = input("please enter the basic number: ")
                num2 = input("please enter the pow number: ")
    elif the_choose == "sqrt":
        the_number = input("enter the number you want to take the sqrt from it: ")
        while True:
            try:
                the_number = float(the_number)
                result = sqrt(the_number)
                print(result)
                break
            except ValueError as err:
                print("please enter only numbers")
                print(err)
                the_number = input("enter the number you want to take the sqrt from it again: ")
    elif the_choose == "exit":
        print("thanks for using this calculator<3")
        os.system('cls')
        time.sleep(3)
        os.system('cls')
        the_answer = "yes"
    else:
        print("enter the only choises i gave you")
