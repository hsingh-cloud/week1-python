# Week 1 - Thursday: Module 3 - Joining Multiple Conditions
# Our IF statement so far focused on single conditions that were satisfied 
# or not. However, we sometimes want a more complicated logic.
# We may want to execute some code when two or more conditions are met 
# at the same time. Or we may want to execute some code when 
# at least one of many conditions is met.
# To that end, we'll use the so called Boolean operators.
# There are three such operators in Python:
# 'and', 'or', 'not'.

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You can apply for a German student exchange program')
else:
    print('Sorry, you do not qualify')

# In the example below, using multiple 'or' conditions
# This time we use the or operator twice.
# The if look will be executed if at least one of the conditions is met 
# in the case of an or operator, Python first evaluates the condition 
# on the left, meaning user country equals Sweden. If this condition is true, 
# Python doesn't even look at the condition on the right.
# Instead it immediately enters the 'IF' block and executes it. 
# However, if the left condition is not met, 
# Python moves on to check the right conditions.

user_country = input('What is your country? ')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify')


user_country = input('Where do you come from? ')
if not user_country == 'Germany':
    print('you are not from Germany!')
else:
    print('you are from Germany')


# Checking conditions using Boolean operators follows 
# Boolean priorities which are:
# 1. NOT
# 2. AND
# 3. OR

# The following is an example: in the 'if not' line, python checks 
# if the user country is not Germany 
# and the age is less than 25  
# if this expression is satisfied, 
# python returns a condition of true.

# otherwise, it checks what is right of the 'or' operator and checks if
# the country is Germany and if the age is less than 23.

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
    user_country == 'Germany' and user_age < 23:
   print('You qualify')
else:
    print('You don\'t qualify')



# Use brackets to improve readability:
 
user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if ((not user_country == 'Germany') and user_age < 25) or \
   (user_country == 'Germany' and user_age < 23):
    print('You qualify!')
else:
    print('You don\'t qualify!')


