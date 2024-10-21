# Module 2 - More about print and strings
# len function - returns the number of characters in a string
# when he introduced the print function, he said that each print and
# vocation adds a new line character at the end.
# That's why these two below were printed on two separate lines:

print('Hello World!')
print('Python speaking!')

# However, you can also change this behavior of the print function.

# If you want to put a full stop at the end of each print invocation, we'll
# use a new feature called KEYWORD ARGUMENTS/NAMED ARGUMENTS

print('Hello World!', end='.')
print('Python speaking!')

print('Hello World!', end='. ')
print('Python speaking!')

# Keyword arguments are arguments which you can use at the end
# of a function invocation.
# After all of the other arguments, they are introduced by using the
# argument name (such as 'end' as seen above) and an equal sign. 

# Keyword arguments are optional.
# Python functions are constructed in such a way that all keyword arguments
# must have default values.

# For example, the end argument for the print function specified 
# what is put at the end of a print invocation
# and has the default value of a new line character.

# If you don't specify the end argument like here, the default value
# will be used instead.
# The default value of the end argument is a new line character.


# One more keyword argument of the print function that you should know
# Sep argument - it specifies the separator between the values printed
# to the output.
# The default value that we have seen so far is a space character.

first_name = 'John'
print('Your first name is', first_name, 'Welcome!')

first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep='-')

first_name = 'John'
print('Your first name is ', first_name, '. Welcome!', sep='"')

first_name = 'John'
print('Your first name is', first_name, 'Welcome!', sep='-', end='=')
