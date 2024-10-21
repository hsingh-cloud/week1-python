# assignment variable
# example below creates a new variable named age and put the value at 28

age = 28
print(age)

# you can also use operators to you assign values to a variable:

age = 28
new_age = age + 5
print(new_age)


# you can also assign a new value to an existing variable

age = 28
age = age + 13
print(age)

age = 28
age +=14 #take current value and add 14
print(age)

age *=2 #take current value and multiply by 2
age -=5 #take current value and minus 5

age = 28
age *= 2
print(age)

age = 30
age -= 5
print(age)

age = 30
age /= 3
print(age) #result is 10.0 which is a float 

# example of string concatenation, which is joining strings

text = 'hokus' + 'pokus'
print(text) #output is hokuspokus

# you can multiply a string by an integer
print('hokus' * 5) #output of this is: hokushokushokushokushokus

# because you can use the plus and multiply operators with strings,
# you have to be extra careful about data types.

print(23+5) #this is standard addition of two integers

# the example below will result in the two strings concatenate together 
# for a result of 235
print('23' + '5') 

