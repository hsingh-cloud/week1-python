# Salary calculator
# Ask the user for the number of hours they worked last month and their hourly rate 
# (both numbers should be floats). Use the following prompts:
# How many hours did you work last month? << add a space at the end of this prompt
# What is your hourly rate? << add a space at the end of this prompt
# Then, show the following message with the calculated salary:
# Last month, you earned {hours * hourly_rate} dollars
# The salary should be shown as a float number. 
# For example, for input 30 hours and hourly rate 10.5, show:
# Last month, you earned 315.0 dollars
# Watch out for typos: you must show the output in this particular format!
# Note: Use the "Run tests" button to check your solution and mark it as complete. 
# Do NOT use the "Run code" button as it will most likely show an error if you use 
# an input() statement.


hours_worked = float(input ('How many hours did you work last month? '))
hourly_rate = float(input ('What is your hourly rate? '))
print('Last month, you earned', (hours_worked * hourly_rate), 'dollars')


# Hints to solve this exercise:
# Remember that you always get a string when you prompt the user with the input() function. 
# Even if the user enters a number like 30.5, Python will treat that as a string '30.5'. 
# You need to use the float() function to transform such a numerical string into a float.

# Coding Exercise 4: Solution -- from the Udemy course:
# Here's a sample solution to Coding Exercise 4:

hours = float(input('How many hours did you work last month? '))
rate = float(input('What is your hourly rate? '))
print('Last month, you earned', hours * rate ,'dollars')

