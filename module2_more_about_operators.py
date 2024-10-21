# Binary operators: in the example below, the plus (+) and minus (-) signs
# work with two operands or two values.
print(5-7)
print(5+7)


# Unary operators: unary plus or minus operators and they work with
# single operands or single values

print(+12)
print(-2)

# Order of Operators - same as in math
# 1. exponentiation (**)
# 2. multiplication and division (* / // %)
# 3. addition and subtraction (+ -)

print(2+3*2) #first multiply 3*2 and then add 2 and this equals 8.

# you can add brackets to change the order of operations

print((2+3)*2) #first add 2+3 and then multiply by 2 to equal 10.

# The precision of floating point numbers in Python
# All data is stored in computer as zero or ones, 
# Most floats cannot be represented exactly as binary fractions.
# As a consequence, the floats that you use in Python are only 
# approximated rounded when they are stored as binary numbers in 
# your computer.
# In other words, the float numbers are more or less right, 
# but they are not 100% correct.
# Example:
print(0.1) # python is rounding this number
print(0.1 + 0.1 + 0.1) # this equals: 0.30000000000000004
# you may think this equals 0.3, but you get 0.30000000000000004.
# the 4 at the end is the lack of precision.
# Remember: The precision of floats is limited. 

# Exponentiation operator
# there are two exponentiation operators and order of operations DOES matter.
print(2 ** 2 ** 3) # equals 256

# REMEMBER: The exponentiation operator (**) uses right-sided binding
# meaning that it starts from the right.


print(8 ** 2) # this equals 64
print(2 ** 8) # this equals 256


# All of the other operators are left-sided bound instead. 








