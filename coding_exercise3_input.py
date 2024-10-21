# Practising input()
# Ask the user to provide their login and native language. Use the following prompts:
# Enter your login: << remember to add a space at the end of this prompt!
# Enter your native language: << remember to add a space at the end of this prompt!
# Then, show the user the following message:
# Your login is {login provided} and you speak {language provided}
# For example, if the user provides the login h_potter and language British English, show:
# Your login is h_potter and you speak British English
# Watch out for typos: you must show the output in this particular format!
#
# Note: Use the "Run tests" button to check your solution and mark it as complete. 
# Do NOT use the "Run code" button as it will most likely show an error if you use an input() statement.

# string apostrophe comma space variable comma space apostrophe
# example: 'Your income is', income, 'and your


print('Enter your login: ')
login = input()
print('Enter your native language: ')
language = input()
print('Your login is', login, 'and you speak', language)


# To get some input from the user and save it to a variable, you can use something like this:
# sample_value = input('Please provide a sample value: ')
# Note that we put a space at the end of the string inside the brackets of input().
# Note: Use the "Run tests" button to check your solution and mark it as complete. 
# Do NOT use the "Run code" button as it will most likely show an error if you use an input() statement.

print('Please enter your login: ')
login = input( )
print('Please enter your native language: ')
language = input( )
print('Your login is', login, 'and you speak', language)


# Coding Solution Answer from Udemy instructor
# Coding Exercise 3: Solution
# Here's a sample solution to Coding Exercise 3:

login = input('Enter your login: ')
language = input('Enter your native language: ')
print('Your login is', login, 'and you speak', language)