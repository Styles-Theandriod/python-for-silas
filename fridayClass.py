person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }


print(person.keys())
print('\n')

print(person.values())
print('\n')

print(person.items())

def message(name, message):
    print(name,message)

message('emmanuel', 'welcome to python')


def sumTwonumbers(num= 1, num2= 15):
    print('sumTwonNumbers',num+num2)
sumTwonumbers()

def sum_all_nums(*args):
    total = 0
    for num in args:
        total += num     # same as total = total + num 
    return total
print(sum_all_nums(2, 3, 5))


def square_number (n):
    return n * n

def do_something(f, x):
    return f(x)
# print(do_something(square_number, 3)) 

print(do_something(9,3))




