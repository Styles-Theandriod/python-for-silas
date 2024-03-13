num = 50

if num > 0 :
    print('num is greater')

if (num > 0):
    pass    


# def main():
#     userInput = int(input('Enter your Age'))

#     if userInput == range(0, 2):
#         print('you are an infant')

#     elif userInput == range(2, 12):
#          print('you are child')

#     elif userInput == range(12, 18):
#         print('you are an adolescent')
#     elif userInput > 18:
#         print('you are an adult')
#     else:
#         pass

# main()


listItems = ['mongo', 'bmw', 'emmanuel', 'bizmarrow']

if 'mongo'  in listItems:
    print('am inside the list')

# = equal to
# == equality 
# != not equal to 
    
# is 
# is not 
# not 
# not not 

item = 50

# if item is not 20:
#     print('am not 20')

if not item > 20:
    print('i am greater than 20')
else:
    print('i am not greater than 20')

if not not item > 20:
    print('i am greater than 20')
else:
    print('i am not greater than 20')



dict = {
        'Name':'emmanuel', 
        'Age':28, 
        'Address':'central area bizmarrow', 
        'Country':'Nigeria'
        }

print(dict.pop('Name'))

print(dict)

print(len(dict))

print(dict['Country'])

dict['Country'] = 'Canada'
print(dict)


print("Age" in dict)

dict.popitem()

# del dict 

# dict.clear()



print(dict.items())

# Using a for loop in a dictionary
nameOfArea = {
    'Area1': 'Area1 shopping center', 
    'Area2': 'Wuse Market', 
    'Area3': 'Phototech Under bread'
    }

for key in nameOfArea:
    print(key)
