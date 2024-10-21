
for counter in range (1,6):
    print('Number:', counter)
    if (counter < 5):
        print('Still counting!')
    else:
        print('Finished!')

# above program results in the following output:

# Number: 1
# Still counting!
# Number: 2
# Still counting!
# Number: 3
# Still counting!
# Number: 4
# Still counting!
# Number: 5
# Finished!

# Translation
# source code -->> machine code
# this translation is either through compilation or interpretation
# compilation: 
#    - compile source code only once
#    - anyone can run the executable file
# interpretation
#    - interpret source code every time you run programs
#    - everyone needs the interpreter to run
#    - scripting languages

# when checking code, python interpreter checks:
#   - lexis, e.g., can't use certain words
#   - syntax, e.g., forgetting the close bracket
#   - semantics, e.g., a function that doesn't accept multiple arguments


## TYPECASTING ##
# Remember: changing between data types (e.g., strings to floats or integer to string)
# is called typecasting.

# Module 2
# Input function always returns a string

# The following function returns an error:
# height_cm = input ('Height converter: enter your height in cm: ')
# print('Your height in feet is:', height_cm / 30.48)

# The function above returns an error because you cannot 
# divide a string (input) by an integer (30.48). 
# So need to find a way to convert the string number into a float number


# float function accepts a string value and tries to convert 
# the string number to a float number
# so we introduce a new variable named float_height_cm

height_cm = input ('Height converter: enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48)

# another way to use the float function for the same function:
# one function becomes the argument of another function:

height_cm = float(input ('Height converter: enter your height in cm: '))
print('Your height in feet is:', height_cm / 30.48)

# integer function takes a string input and tries to convert it to an integer


year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')


# reverted function - it converts an integer or a float into a string. 
# it is not used as often but it is useful when you want to include the results of 
# some calculations in a string.

temp_c = input('Enter the temperature today in Celsius degrees: ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + ' degrees Fahrenheit.'
print(temp_statement)
