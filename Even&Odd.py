def check_even_odd(number):
    if number % 2 == 0:
        print("{number} is even")
    else:
        print("{number} is odd")

check_even_odd(2)

def our_loop():
    for i in range(0,20,4):
        print(i)
our_loop()


lst = list(range(11))
print('this list', lst)


# Accessing items inside a list using for loop
# for i in len(lst) :
#     print(i)

print("\n")
for i in lst:
    i += 1
    print(i)

# Slicing a list
items = list(range(20))

# print(items[0:10])

for i in items:
    print(items[0:10])
    break
    # i += 1

# While Loop

count = 1

while count <= 5:
    print(count)
    count += 1


# while True:
#     userInput = input('Type Quit to exit program')

#     if userInput.lower() == 'quit':
#         break
#         print('you have exited the loop')

# Basic functions and uses 
title = 'this is a test program'

number = [1,2,400]
print('a text', len(title))

print('this is a max function', max(number))
print('this is a Min function', min(number))
print('this is a Sum function', sum(number))


empty_tuple = (12,4)
empty_tuple = tuple()

tuple = ('item1', 'item2', 'item3')
print(len(tuple))

print(tuple[-1])

# slicing a tuple 
allitems = tuple[2:]
print(allitems)

tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[-4:]         # all items
print('this is all_items', all_items)

middle_two_items = tpl[-3:-1] 
print('middle_two_items', middle_two_items)

old_tuple = (2, 3, 4, 5, 6, 7, 8, 9)
new_tuple = list(old_tuple)
print( new_tuple)


Bulb = False
# userInput = input('on or off the bulb')
# if(userInput == 'on'):
#     Bulb = True
#     print('the bulb is on')
# elif(userInput == 'off'):
#     Bulb = False
#     print('the bulb is off')
# else:
#     pass

print('\n')

def MTN():
    print('\tChoose a Data Plan')
    print('1: Daily Plan')
    print('2: Weekly Plan') 
    print('3: Monthly Plan')
    print('4: Yearly Plan')

    UserInput = input('Enter a plan')
    if UserInput == '1':
        print('1gb : 600₦')
        

def Mobile9():
    print('\tChoose a Data Plan')
    print('1: Daily Plan')
    print('2: Weekly Plan')
    print('3: Monthly Plan')
    print('4: Yearly Plan')

def Glo():
    print('\tChoose a Data Plan')
    print('1: Daily Plan')
    print('2: Weekly Plan')
    print('3: Monthly Plan')
    print('4: Yearly Plan')

def Airtel():
    print('\tChoose a Data Plan')
    print('1: Daily Plan')
    print('2: Weekly Plan')
    print('3: Monthly Plan')
    print('4: Yearly Plan')

def message():
    print('\twelcome Leke Data Sevice')
    print('1: MTN Data Sevice')
    print('2: 9Mobile Data Sevice')
    print('3: Glo Data Sevice')
    print('4: Airtel Data Sevice')
    UserInput = input('Enter a number')
    if UserInput == str(1):
        MTN()
    elif UserInput == str(2):
        Mobile9()
    elif UserInput == str(3):
        Glo()
    elif UserInput == str(4):
        Airtel()



def UserInput():
    UserInput = input('Dail the code')
    if UserInput == '*123#':
        message()
    else:
        pass
UserInput()









