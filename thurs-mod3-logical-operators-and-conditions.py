# Week 1 - Thursday: Logical Operators & Conditions

# available logical operators
# <   less than
# >   greater than
# <=  less than or equal to
# >=  greater than or equal to
# ==  equals
# !=  not equals

password = input('Do you know the secret password? ')
if password != '--secret':
    print('not correct')
else:
    print('correct passwod')

# Now, when Python sees a condition with one of the logical operators, 
# it checks whether the condition is met or not.
# The result is always a boolean value.
# We've already discussed Boolean values, but let's revisit them now.
# A boolean variable can have one of two values: True or False
# Note that we do not use quotes around the words true and false.
# If you use quotes, you'll get a string instead of a boolean.
# You must also remember to start the words true and false with capital letters.
# So for example, condition equals true.
# This is a correct assignment, but if we change it to a small letter, 
# you can see a name error.
# True and false are the only values available in a boolean.


# Remember:
# = (single equal sign) means assigning values
# == (double equal sign) means checking equality


if 2 == 2:
    print('true')

if 1 == 2:
    print('true')

if 2 == 2.0:
    print('true')

