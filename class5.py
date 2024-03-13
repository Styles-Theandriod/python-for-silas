

# Person = {'name': 'John', 'last_name': ' Doe', 'Age': 36}

# print(Person['name'])
# print(Person)

# items = list()
# empty_list = []
# print(empty_list)

# fav_food = [ 'pounded yam', 'rice with chicken', 'Banga soup and stach', 'Beans' ]

# cars = ['Tesla', 'Benz', 'Mustang', 'Mustang', 23490582388, True,]

# countries = ['Canada', 'Sweeden', ' Portugal', 'Silicon Valley In USA',]
# print(cars[-1])


# # UnPACKING A LIST 

# artist = ['Chris brown', 'Psquare', 'Wiskid', 'Rema']
# first_artist, second_artist, *rest = artist
# # print(first_artist, second_artist)
# print(first_artist, second_artist)

# fav_football_players = ['Nwabai', 'Messi', 'Ronaldo', 'Nema', 'Osimehn']
# fav_football_players = ['Nwabai', 'Messi', 'Ronaldo', 'Nema', 'Osimehn']


# # print(artist[0:3])
# # print(artist[:-1])
# # print(artist[::2])
# # print(artist[-3:-1])
# print(fav_football_players[-1:-3])
# print(fav_football_players[-1:-3])
# print(fav_football_players[-1:-3])
# print(fav_football_players[-1:-3])
# print(fav_football_players[-1:-3])
# print(fav_football_players[-1:-3])

# # changing items in a list
# phones_models = ['Iphone', 'Samsung', 'Hawaii', 'Oppor']

# changed_items = phones_models[3] = 'itel'
# print(changed_items)

# # Adding items to the list

# phones_models.append('infinise')

# print(phones_models)

# # Popping items in the list
# fav_drinks = ['Coca Cola', 'Bigie', 'fanta']

# fav_drinks.pop(0)
# fav_drinks.pop()

# print(fav_drinks)


# # Deleting items in the list
# brands = ['gucci', 'vasscii', 'dng', 'fendi', 'theandriod']
# del brands[0:2]

# print(brands)

# # List comprehension
# language = 'python'
# lst = [language]
# print(lst)


# # Python game creation 

# # checks data from thinking with user input if they match returns True


# userInput = float( input('Enter your year of birth: '))

# currentYear = 2024

# print('Your current age is: ', userInput - currentYear)



# import random

# database = []  # Make database a global variable
# print(database)

# def Game():
#     while True:
#         score = 0

#         thinking = ['education', 'coding', 'science', 'Programming', 'Fathering', 'Mothering', 'sisters']
#         computer_thinking = random.choice(thinking)

#         userInput = input('What am I thinking: ')

#         if userInput == computer_thinking:
#             print('You got my thinking 😂')
#             score += 1
#         else:
#             print('Wrong! Try again 😭')

# def createAccount():
#     print('#1 Create Account \t  #2 Login Account')

#     userInput = input('Enter a number: ')

#     if userInput == str(1):
#         username = input('Enter username: ')
#         password = input('Enter password: ')
#         database.append({'username': username, 'password': password})
#         Game()
#     elif userInput == str(2):
#         username = input('Enter username: ')
#         password = input('Enter password: ')
#         if any(entry['username'] == username and entry['password'] == password for entry in database):
#             Game()
#         else:
#             print('Invalid credentials. Try again.')

# createAccount()



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
#         print('your score is ' + str(score))
#     else:
#         print('wrong try again 😭')
#         score = score - 1

#     play_again = input('Do you want to play again? (yes/no):').lower()
#     if(play_again != 'yes'):
#         break;



sentence = 'i love tech'
# print(sentence[0]) #indexing
print(sentence[0:12]) #slicing 

# Escape characters in python 
print('i am a programmer \n living in Abuja')
print('i am a programmer \t living in Abuja')

# Numbers Math Operators



num = 30

print('Addition',num + 5)
print('Subtraction',num - 5)
print('Multiplication',num * 5)
print('Division',num / 5)
print('floor ',num // 5)
print('Modulus',num % 5)

# Random Numbers in python 
import random

# words = ['education', 'asake', 'mr ibu', 'Tinubu', 'Aki', 'pawpaw']
# thinking = random.choice(words)

# userInput = input('what am i thinking')

# if(userInput == thinking):
#     print('You got my thought')
# else:
#     print('Try again Later')


# done with that area 
print(random.randint(0,10))

# Math Lib/functions
import math

print(math.cos(2))
print(math.sqrt(2))
print(math.sin(2))
print(math.tan(30))

# List in python 
footballers = ['Ronaldo', 'messi', 'Bruno', 'mpape']

print(footballers[-1])

# Changing items in a list
footballers[0] = 'emmanuel'

# Adding items to the list
footballers.append('chidimma')

# Deleting items in the list
footballers.pop(0)
footballers.remove('chidimma')
print(footballers)

# List comprehension
lst = ['pawpaw', 'orange', 'mango']

item1, item2, item3 = lst 

print(item1)

# Functions in python 
def SayHello(message, *names):
    print(message, names)

SayHello('hello', 'emmanuel', 'peter',)

def greet(name, greeting="Hello"):
    print(greeting, name)

greet('Alice')

# Downloading an image from online
# import requests

# def download_image(url, destination):
#     response = requests.get(url)
#     if response.status_code == 200:
#         with open(destination, 'wb') as file:
#             file.write(response.content)
#         print(f"Image downloaded successfully to {destination}")
#     else:
#         print(f"Failed to download image. Status code: {response.status_code}")

# # Replace 'image_url' with the URL of the image you want to download
# image_url = 'https://picsum.photos/300/300'

# # Replace 'destination_path' with the desired location and filename to save the image
# destination_path = 'image/image.jpg'

# download_image(image_url, destination_path)



# Classess In Python 

from pythonWithSilas import Dog 






# User Input in python

# accepting numerica user_input
# userInput = int( input('Enter your number'))
# print(userInput + 2)

userInput = float( input('Enter your number'))
print(userInput + 2)


def is_multiple_of_four(number):
    return number % 4 == 0

# Examples
number1 = 16
number2 = 7

if is_multiple_of_four(number1):
    print(f"{number1} is a multiple of four.")
else:
    print(f"{number1} is not a multiple of four.")

if is_multiple_of_four(number2):
    print(f"{number2} is a multiple of four.")
else:
    print(f"{number2} is not a multiple of four.")

# Generating numbers using the range function



# Files and Exceptionsin python 
# Reading from a File

file_path = 'file.txt'

# try:
#     with open(file_path, 'r') as file:
#         content = file.read()
#         print('File content: {}'.format(content))
# except FileNotFoundError:
#     print(f"File not found at {file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")


# item = open(file_path, 'r')
# print(item.read())

file_path = 'file.txt'
content = 'I am new content.'

# Open the file in append mode ('a')
with open(file_path, 'a') as file:
    file.write(content)


item = open(file_path, 'r')
print(item.read())

# Exceptions
# try and except 

try:
    result = 10 / 0

except ZeroDivisionError:
    # Handle the exception
    print("Cannot divide by zero.")
finally:
    # Code to be executed regardless of the exception
    print("Execution completed.")






