print('Learning about variables, how they work, and how to use them.\n')


'''
 Im going to break this down into 3 parts, Simple, Intermediate, and Advanced Variables.
 With that being said; The main reason that I would like to do this is the even tho all of these Variable types are
 equally important, so may be harder to understand and fully grasp.
 
 Note: Please disregard Empty `Print()` functions as they are used for spacing in the terminal.
'''

'''
 Simple:
 
    Strings; A string is a combination of chars or characters. chars can range from a-z, A-Z, 0-9, or even most special
    characters like '?,.<>;: Etc...'. Strings are defined by putting quotes or double qoutes around the characters that 
    are to be included.
    
    Int; An Int is a number that can be positive or negative.
    
    Bool; Boolean variables have either two states, This is either True or False.
    
    None; None is a special beast.. Well not really.. None is exactly what it sounds like, its nothing.
'''

# String
message = 'I am a String!'
print('String: {}'.format(message))

'''
 For more information on Strings please see the Strings.py file.
'''
# Todo Create Strings.py.

# Int
real_int = 20
print('Real Int: {}'.format(real_int))

float_int = 20.053
print('Float Int: {}'.format(float_int))

'''
 For more information on Ints please see the Numbers.py file.
'''
# Todo Create Numbers.py.

# Bool
boolean = True
print('Boolean: {}'.format(boolean))


print()

'''
 Intermediate: 
    
    List: A list is exactly what it sounds like, Its a list of items. This can be Strings, Ints, Other lists, Anything.
    
    Tuple: Much like a List a tuple is a list of items, the main difference being the Tuples are read-only meaning once
    they are created they can not be modified or updated.
    
    Dictionary: A dictionary again is like a List or Tuple except it uses Key:Value pairs.
'''

# List

list_var = ['Hello', 'their', 'I\'m', 'a', 'List']

for l in list_var:
    print(l)

print()
# Tuple

tuple_var = ('Hello', 'their', 'I\'m', 'a', 'Tuple')

for t in tuple_var:
    print(t)

dict_var = {'1': 'Hello', '2': 'their', '3': 'I\'m', '4': 'a', '5': 'Dict'}

for k, v in dict_var.items():
    print('{}: {}'.format(k, v))

'''
 For more information on Loops such as the `for` loop please see the Loops.py file.
 For more information on Dictionaries please see the Dictionaries.py file. 
'''
# Todo Create Loops.py and Dictionaries.py file.

print()

'''
 Advanced:
    Custom: These are variable types that can be created custom by you.
'''

# Custom


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'My name is {} and I\'m {} years old.'.format(self.name, self.age)


my_person = Person('Joe', 16)
print(my_person)

'''
 For more information on Classes please see the Classes.py file.
'''
# Todo Create Classes.py file.
