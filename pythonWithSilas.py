print('welcome to python class')

# Variable naming in python 
# snakeCase 
# PascalCase
# CamelCase 


First_Name = 'emmanuel' #SNAKE CASE
lastName = 'forest' # camel case
NewAge = 23 # PASCAL CASE

First_Name = 'onyekachi'
print(First_Name)


# case functions in python 
print(First_Name.upper())
print(First_Name.lower())
print(First_Name.title())
print(First_Name.capitalize())

# datatypes in python
# strings 
# intergers
# float 
# set  
# list 
# tuple 
# dict
# complex 
# boolean 

setOfNumbers = {1, 2, 3}
print(setOfNumbers)

Numbers = [1, 2, 3, 4, 5, 6, 7]

myTuple = ('Dangote', 'Patricia', 'darey abegapp')
Dictionary = {'Name': 'Dangote', 'Type': 'Business'}
myComplex = 10+1j
hammantan = True

print('this is the length', len(myTuple))

""" this is another comment """
''' this something wired '''

# string new topic 
first_text = 'this is some content'
second_text = 'this is another content'

# concatenation 

newText = first_text + second_text
print(newText)

print(int('30') + 1)

int 
float 
str 
list 
dict 
set 
complex

# indexing of a string 
myword = 'today is python'
print(myword[0])

# slincing of a string in python 
print(myword[3:-1])

print('\n')
print('\t hello world')

print("In every language \"hello world\" comes first ")

print('this is a blackslash \\\\\\')

# userInput = input('enter your username')

# print('your name is', userInput)

First_name = 'chidera'
lastName = 'omahlay'

formatted_string = 'my name is {} {}'.format(First_name, lastName)
print( formatted_string)

a = 3
b = 3

print('{} + {} = {}'.format(a, b, a+b))

radius = 10
pi = 3.14
area = pi * radius ** 2 
formatted_string = 'The area of a circle {} is {:.3f}'. format(radius, area)
print(formatted_string)


# Math operator Numbers 
# Arithmetic operator 
# Assignment operator

# Addition (+)
# substraction (-)
# Modulus (%)
# Divison (/)
# exponetial (**) 
# Multiplication (*)
# floor division (//)

num_one = 40
num_two = 50

total_num = num_one + num_two
print(total_num)

# substractions 
total_num = total_num - num_one

# modulus 
total_num = total_num % num_one

# Divison
total_num = total_num / num_one

# exponetial 
total_num = total_num ** num_one

# Multiplication
total_num = total_num * num_one

# floor division 
total_num = total_num // num_one

# assignment operators

x = 4
y = 10

# x = x + y

# x += y

# comparison operators 
print(type(x) is type(y))
print(not not not not x <  y)

# = 
# ==
# != 
# <
# >
# &
# and 

import random

# score = 0
# thinking = ['education', 'family', 'children', 'omah', 'Bizmarow']

# random_thinking = random.choice(thinking)

# print(random_thinking)
# userInput = input('what am i thinking about')


# if userInput == random_thinking:
#     print('You got my thought 😍')
# else:
#     print('Try again next time')


print(random.randint(1, 10))

print(random.random())

import math

print(math.cos(2))
print(math.sqrt(2))
print(math.sin(2))
print(math.tan(30))



# list in python 

items = [1, 2, 3, 4, 5, 6, 7, 8, 9]

fruits='apple', 'orange'

print(list(fruits))


# changing items in a list 
items[0] = 'pawpaw'
print(items)

# Adding items to the list

items.append('oranges')
items.insert(3, 'fishes')
print(items)

# Popping items in the list
items.pop()
print(items)

# Deleting items in the list

items.remove(4)
print(items)

# del items

items.copy()
items.clear()

# List comprehension
listItems = ['bmw', 'canmery', 'honda', 'mercedes' ]

item1, items2, items3, items4 = listItems

print(item1)
print(items2)

language = list('python')

print(language)
print(len(language))
print(type(language))


even_numbers = [i for i in range(21) if i % 2 == 0]
odd_numbers = [i for i in range(21) if i % 2 != 0]

print(even_numbers)



# i = range(0, 21)
# print(list(i))

# scope 
# if statement
# elif statement
# def 
# userInput


# userInput = float(input())
# userInput = int(input())

# Generating numbers using the range function

for i in range(0, 12):
    print(i)

# Accessing items inside a list using for loop
myList = ['apple', 'pawpaw', 'oranges', 'mango', 'banana', 'guava', 'watermelon']

for i in myList:
    print(i)

print('\n')

for i in myList[0:6:2]:
    print(i)

    
# apple 
# oranges 
# guava 
    
# The while Loop in Action

num = 0

# while num <= 10:
#     print(num)
#     num += 1

# Letting the User Choose When to Quit



# import random

# thinking = ['gucci', 'education', 'fendi', 'theandriod', 'dng', 'jadrolita', 'bizmarrow']


# while True:

#     random_thinking = random.choice(thinking)

#     print(random_thinking)

#     print('what am i thinking about')

#     userInput = input('Your guess: ')

#     score = 0

#     if(userInput  in random_thinking):
#         print('you got my thought 😂')
#         score = score + 1
#         print('your score is ' + ' ' + str(score))
#     else:
#         print('wrong try again 😭')
#         score = score - 1
#         print('your score is ' + ' ' +  str(score))

#     play_again = input('Do you want to play again? (yes/no):').lower()
#     if(play_again != 'yes'):
#         break;



num = 20

while num < 200:
    num = num + 1
    if(num == 50):
        continue;
    print(num)


# print(len(num))

intMax = [20, 30, 40, 50, 60,]

print(max(intMax))
print(min(intMax))
print(sum(intMax))


Mytuple = (1, 2, 3, 4, 5)
print(Mytuple)



num = 20

if num == 10:
    print('the number  is 10')
elif num == 20:
    print('the number  is 10')
else:
    print('i dont know the value ')


lst = ['emmanuel', 'bizmarrow']

if('bizmarrow' in lst):
    print('i am there')
else:
    print('i am not there')



# Dictionary 
dict = {'name': 'emmanuel', 'Age': 30}

for j in dict.values():
    print(j)


def greeting(name, greet):
    print(greet, name)


def another():
    greeting('Mr emmanuel', 'Good evening')

another()


def arbitrary(name, *greeting):
    print(greeting, name)

arbitrary('emmanuel' , 'Good night', 'good day')



# downloading an image from online 
# import requests
# def download_image(url, destination):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(destination, 'wb') as file:
#             file.write(response.content)
#         print(f'Image downloaded successfully to {destination}')
#     else:
#         print(f'Image download failed. status: {response.status_code}')

# image_url = 'https://picsum.photos/300/300'
# destination_path = 'image/image.jpg'

# download_image(image_url, destination_path)

# Making an argument optional
def optionalAgument(name='emmanuel', Age=30):

    print(name, Age)

optionalAgument()

# Class in python 

class Dog:
    def __init__(self, name, age, walking):
        self.name = name
        self.age = age
        self.walking = walking

    def bark(self):
        print(f"{self.name}")
    
    def walk(self):
        print(f"{self.walking}")
    

My_dog = Dog(name="chitar", age=300, walking='my dag is walking')

My_dog.bark()


# Files and Exceptions

# Reading from a File

file_path = 'silas.txt'
item = open(file_path, 'r')
print(item.read())

# Writing to a File

content = 'this is a new contentsssssssssssssssssssssssssssssssssssss'
with open(file_path, 'a') as file:
    file.write(content)



# Exceptions
# Try-except blocks
try:
    result = 10 / 0

except ZeroDivisionError:
    print('cannot divide by Zero')
finally:
    print('done')


# Date and time function
    
import datetime

d = datetime.datetime.now()

my_date = datetime.date(2015, 1, 1)
my_time = datetime.datetime(2024, 10, 31, 20, 10, 15)

# my_time.strftime("% %d %b %Y %H:%M:%")

print(my_time)


import pymongo


# Replace the connection string with your MongoDB connection string
client = pymongo.MongoClient(f"mongodb+srv://theandriod:{}@theandriod.i5wb5np.mongodb.net/?retryWrites=true&w=majority&appName=theandriod")

d = client['school_db']

collection =d['school_collection']

# insert a documents collection
data = {"key":'value', 'another_key':'another_value'}

# insert_data = collection.insert_one(data)


# result = collection.find()

# for i in result:
#     print(i)

# query_critera = {"Age": {"$gt": 25}}

# result = collection.find(query_critera)

# for i in result:
#     print(i)


# print(f"Inserted document Id: {insert_data.inserted_id}")




bizmarrow_students = collection.find({"school": "Bizmarrow"})
for student in bizmarrow_students:
    print(student)


# Sort in python mongodb
bizmarrow_students = collection.find().sort('age', pymongo.DESCENDING)
print('students age are sorted in descending order')

for student in bizmarrow_students:
    print(student)


multiple_sort_students = collection.find().sort([("age", pymongo.ASCENDING), ("name", pymongo.DESCENDING)])

for i in multiple_sort_students:
    print(i)

# Delete/ Drop in python mongodb 
    
# bizmarrow_students = collection.drop('name')
bizmarrow_students = collection.drop() #drop a collection

delete_result = collection.delete_one({"name": "emmanuel"})

delete_result = collection.delete_many({"age": {"$gt": 20}})

delete_result = collection.delete_many({}) 
# delete all the documents collection


# Update in python mongodb
update_result = collection.update_many(
    {"age":30},
    {"name":'emmanuel'}
)
update_result = collection.update_many(
    {"name": "John"},
    {"$set": {"age": 30}}
)

# Limit in python mongodb
limited_result = collection.find().limit(3)
