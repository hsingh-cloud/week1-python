# each variable has its own type

# SECTION: Data Types

# Data type = String
greeting = 'Hello, friend!'
# greeting variable has data type of string because
# it is surrounded by apostrophes

# Data type = Integer
age = 35
# age is a variable with data type of integer because
# it is NOT surrounded by apostrophes

# Data type = Floats
# floats are numbers that have a decimal fraction 
# introuduced with a dot. 
# once we introduce a dot, our integer number becomes 
# a float, even if the decimal part is zero.

# the following three examples are all floats. 
# speed2 and speed3 are the same.
# speed4 is an integer because there is no float.
speed1 = 4.5
speed2 = 4.0
speed3 = 4.
speed4 = 4

# Data type = Boolean
# a Boolean value is either true or false
# true or false must start with a Capital letter so 
# must use a Capital letter to introduce a Boolean value

am_i_ugly = True

# Remember this programming rule:
# True = 1
# False = 0

print(am_i_ugly) # here is a midline comment
print('am I ugly')
print(am_i_ugly)

# note the variables are strings and not numbers:
var1 = '23'
var2 = '54'

print(var1)

# SECTION: NUMERICAL REPRESENTATION
# two basic numerical types: integers & floats

# Underscore in numbers
# can use underscores in numbers. can't use dots, commas, or separators
# for example: 120000000 can be written as 120_000_000

# Scientific notation
# 3e4 = 3E4 = 3 * 10000 = 30000
# 3e-4 = 3E-4 = 3 * 1/10000 = 0.0003

print(3e-4) #result of this function is 0.0003

# Integer numbers can be respresented as octal numbers or hexidecimal numbers

# Octal value: if a number starts with zero capital O or zero small o
# The digits that follow the zero zero prefix must be from the range from 0 to 7
# for example, this "print(0o123)" which is the same as 83 in the 
# standard decimal representation

print(0o123)
print(0O123)

# Hexadecimal numbers are preceded by either zero capital x or zero small x
# for example 0X123 is equal to 291 in standard decimal system

print(0x123)
print(0X123)


# SECTION: Operators

# special symbols to perform mathematical operations

# three types of division:
# standard division
# integer division
# modulus operation (modulo division)

# I) standard divison - use integers to divide but the result is always a float number
# 6 / 2 = 3.0
# 7 / 2 = 3.5

print(6/2) # this produces a result of 3.0
print(6 / 2) # this produces a result of 3.0

# II) integer division - always returns the nearest whole number rounded down
# 6 // 2 = 3
# 7 // 2 = 3

print(6//2) # result is 3
print(7//2) # result is rounded down to 3

# integer division (//) always returns the nearest whole number rounded down. 
# Keep in mind, however, that this whole number might be of type integer or float, 
# depending on your input numbers:
# 6 // 3     # returns 2
# 6.0 // 3   # returns 2.0
# 6 // 3.0   # returns 2.0
# 6.0 // 3.0 # returns 2.0

# If you integer divide two integers, the result is of type integer. 
# # But if at least one of the input numbers is a float, you will get a float instead. 
# The same rule applies to all other operators except for the standard division (/), 
# which always returns a float, even for two integers.


# III) modulus division - returns the remainder of the division 
# example 1: 6 % 2 is zero because you can divide 6 by 2 and there is nothing left
# example 2: 7 % 2 is one because 7 divided by 2 is 3 with a remainder of 1
# In general, if you have x % y, and the second number y is greater than the first number x, 
# the result will always be x: 7 % 16 = 7


print(6%2) # result of this function is zero
print(7 % 2) # result of this function is one



# power operator - introduced with two stars
# example: 2 ** 3 equals 8

print(2**3) # result is eight


# if you use all integers, your result will be an integer
# if you use one float and rest integers, your result will be a float
# if you use two floats, you will get a float

print(10+3.0) #result is 13.0



