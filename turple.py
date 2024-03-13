
myTurple = (0, 2, 3 , 2, 2, 6, 7, 8, 9, 10)

# data type 
print(type(myTurple))

# print(myTurple.count(2))
print(myTurple.index(3))

# logical statements in python

number = 100

if number == 50 :
    print('yes i am greater than 50')
elif number == 100:
    print('yes my value is 100')
else:
    print('i dont understand')


# using the if function for a list
lst = [10]

if lst == [10]:
    print('yes i am there')
else:
    print('notting worked!!')


# Equality and Inequality Symbols
# Equality == 
# Inequality !=
# is 
# not 
# is not
# in 
    

LuckyNumber = 20

if LuckyNumber != 50:
    print('LuckyNumber is not equal to 50')
else:
    print('LuckyNumber is equal to 50')


# print(20 is not  50)
    
# print(not not not 20  is  50)

# Dictionaries in python 
person = {'Name':'emmanuel', 'Age':18, 'skinColor':'red'}

for i in person.keys():
    print(i)

for i in person.values():
    print(i)

for i in person.items():
    print(i)


# function in python 
def greet():
    print('Good Morrrring Sir')

greet()


num = 0

while num < 10:
    greet()
    num += 1

greet()

# Parameters and Arguments in python 
def msg(message):
    print(message)

msg('Hello world')

# Arbitrary arguments in python 
def welcome(name='emmanuel', message='welcome mr'):
    print(message, name)

welcome()

# Making an argument optional
def welcome(name='emmanuel', message='welcome mr'):
    print(message, name)

welcome('ogechi', 'hello')

# Introduction to libraries
# pip install library name

# Downloading an image from online
import requests
    