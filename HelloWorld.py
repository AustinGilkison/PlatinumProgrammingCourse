print('Learning how to print messages with the print function.\n')

'''
 Printing 'Hello World' to the terminal.
'''
print('Hello World')
'''
 Simply using the `print()` function we are able to print anything we need to the terminal.
'''


''' 
 Printing 'Hello World' to the terminal using a variable to hold the string value of "Hello World".
'''
message = 'Hello World'
print(message)
'''
 By assigning the variable `message` the value 'Hello World' we are able to pass `message` to the `print()` to print 
 its value 

 For more information on variable and how they work and are used have a look into the `Var.py` file.
'''

'''
 Printing by passing a string into a custom print function called `print_me()`.
'''


def print_me(print_message):
    """
     Prints the value of the print_message var.
    :param print_message: Message to be printed.
    """
    print(print_message)


print_me('Hello World')

'''
 We call the `print_me()` function and pass it the variable or data that we would like to print, in this case being
 'Hello World'. Once this function has been called it then calls the `Print()` function the in turn prints our message
 or data.
 
 For more information on Functions please see the `Func.py` file.
 For more information on Doc strings please see the `Doc.py` file.
'''
# Todo Create Func.py and Doc.py
