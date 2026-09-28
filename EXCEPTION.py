# try:
#     # risky code
# except:
#     # runs if an exception occurs
# else:
#     # runs only if NO exception occurs
# finally:
#     # runs ALWAYS
import math

# try:
#     a = int(input("Enter a number: "))
#     print(10 / a)
#
# except ZeroDivisionError:
#     print("Cannot divide by zero")
#
# except ValueError:
#     print("Enter numbers only")
#
# else:
#     print("Operation successful")
# #
# # finally:
# #     print("Program completed")
#
# def read():
#     try:
#         fi = input("ENTER THE FILE NAME ")
#         f = open(fi, 'r')
#         print(f.read())
#     except:
#         print("FILE DOES NOT EXIT")
#
# def write():
#     try:
#         fi = input("ENTER THE FILE NAME ")
#         f = open(fi, 'w')
#         d = input("ENTER DATA: ")
#         f.write(d)
#         f = open("k.txt", 'r')
#         print(f.read())
#     except:
#         print("FILE DOES NOT EXIT")
#
# def append():
#         fi = input("ENTER THE FILE NAME ")
#         f = open(fi, 'a+')
#         d = input("ENTER DATA: ")
#         f.write(" " +d)
#
# def search():
#     try:
#         fi = input("ENTER THE FILE NAME ")
#         f = open(fi, 'r')
#         d = input("ENTER WORD TO SEARCH: ")
#         c = f.read()
#         if d in c:
#             print("WORD IS FOUND")
#         else:
#             print("WORD IS NOT FOUND")
#     except:
#         print("FILE DOES NOT EXIT")
# def delete():
#     try:
#         fi = input("ENTER THE FILE NAME ")
#         import os
#         os.remove(fi)
#     except:
#         print("FILE DOES NOT EXIT")
#     else:
#         print("FILE DELETED")
#

# while(1):
#     print("------------------------------------------")
#     print("\n 1.FILE READ \n 2.FILE WRITE \n 3.FILE APPEND\n 4.FILE SEARCH \n 5.FILE DELETE \n 6.EXIT \n ")
#     print("------------------------------------------")
#     i = int(input("ENTER YOUR CHOICE: "))
#     if i==1:
#         read()
#     elif i==2:
#         write()
#     elif i==3:
#         append()
#     elif i==4:
#         search()
#     elif i==5:
#         delete()
#     elif i==6:
#         exit()
#     else:
#         print("\nENTER A VALID NUMBER")

#------------------------------------------------ HOMEWORK---------------------------


# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
# import math
# while True:
#     try:
#         n1=int(input("ENTER A NUMBER: "))
#         print(math.factorial(n1))
#         break
#     except ValueError:
#         print("ENTER VALID NUMBER")

#
# def fac():
#     try:
#         n1 = int(input("ENTER A NUMBER: "))
#         print(math.factorial(n1))
#     except ValueError:
#             print("ENTER VALID NUMBER")
#             fac()
# fac()


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.
# import sys
# def addnum(n1, n2):
#     s = n1 + n2
#     return s
# def mulnum(n1, n2):
#     s = n1 * n2
#     return s
# def divnum(n1, n2):
#     s = n1 / n2
#     return s
# def subnum(n1, n2):
#     s = n1 - n2
#     return s
# while(1):
#     try:
#         op = input("ENTER THE OPERATIONS('+','*','-','/',exit: ").strip().lower()
#         # if op=="exit":
#         #     break
#         # a = int(input("ENTER FIRST NUMBER: "))
#         # b = int(input("ENTER SECOND NUMBER: "))
#         if op == '+':
#             a = int(input("ENTER FIRST NUMBER: "))
#             b = int(input("ENTER SECOND NUMBER: "))
#             p = addnum(a, b)
#             print(p)
#         elif op == '-':
#             a = int(input("ENTER FIRST NUMBER: "))
#             b = int(input("ENTER SECOND NUMBER: "))
#             p = subnum(a, b)
#             print(p)
#         elif op == '*':
#             a = int(input("ENTER FIRST NUMBER: "))
#             b = int(input("ENTER SECOND NUMBER: "))
#             p = mulnum(a, b)
#             print(p)
#         elif op == '/':
#             a = int(input("ENTER FIRST NUMBER: "))
#             b = int(input("ENTER SECOND NUMBER: "))
#             p = divnum(a, b)
#             print(p)
#         elif op == 'exit':
#             sys.exit()
#         else:
#             print('INVALID OPERATION')
#     except ValueError:
#         print("INVALID INPUT")
#     except ZeroDivisionError:
#         print("CANNOT DIVIDE BY ZERO")
#     except SystemExit:
#         print("CALCULATOR CLOSED")
#     except:
#         print("ERROR")

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# # exist
# try:
#     f=open('file.txt','r')
#     # f = open('k.txt', 'r')   ###3 file doesn't found
#     print(f.read())
# except FileNotFoundError:
#     print("file does not exist")
#
# else:
#     print("file opened")

# try:
#     fn=input("ENTER FILE NAME: ")
#     f=open(fn,'r')
#     print(f.read())
# except FileNotFoundError:
#     print("FILE DOES NOT EXIST")
# else:
#     print("FILE OPENED")
#

#Given a Dictionary

# d={"name":"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
# try:
#     k=input("Enter a Key:")
#     print("Value=",d[k])
# except KeyError:
#     print("key doesn't found")
# _____________________________________________________________________________TO RAISE A EXCEPTION
# try:
#     n=int(input("enter the age :"))
#     if(n<18):
#         raise Exception("NOT ELIGIBLE FOR VOTING")
#     else:
#         print("ELIGIBLE FOR VOTING")
# except Exception as e:
#     print(e)

#______________________________________________________________________________ FOR CUSTOM EXCEPTION

# class Myaswin(Exception):
#     pass
# try:
#     n=int(input("enter the age :"))
#     if(n<18):
#         raise (Myaswin("NOT ELIGIBLE FOR VOTING"))
#     else:
#         print("ELIGIBLE FOR VOTING")
# except Myaswin as e:
#     print(e)


#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"

# try:
#     n=int(input("ENTER A NUMBER: "))
#     if(n<=0):
#         raise ValueError("NUMBER MUST BE POSITIVE")
#     else:
#         print("ACCEPTED")
# except ValueError as e:
#     print(e)
#

#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
class InvalidPasswordError(Exception):
    pass
try:
    n=input("ENTER THE PASSWORD: ")
    if(len(n)<8):
        raise InvalidPasswordError("PASSWORD SHOULD BE 8  CHARACTERS")
except InvalidPasswordError as e:
    print(e)


#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")

# class InsuffientBalanceError(Exception):
#     pass
# try:
#     bal=5000
#     n=int(input("ENTER THE AMOUNT: "))
#     if(n<bal):
#         raise InsuffientBalanceError("NOT ENOUGH BALANCE.TRANSACTION FAILED")
# except InsuffientBalanceError as e:
#     print(e)
