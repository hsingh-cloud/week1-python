# joining multiple conditions example

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

