income = 250_000
lowtaxland_rate = 0.05 # income tax rate for Lowtaxland
ripoffland_rate = 0.43 # income tax rate for Ripoffland
lowtaxland_result = income * lowtaxland_rate
ripoffland_result = income * ripoffland_rate
difference_tax_amount = ripoffland_result - lowtaxland_result


print('The tax rates are', lowtaxland_rate, 'and', ripoffland_rate)

# This solution uses the plus (+) sign to concatenate. The use of the plus sign was from freecodecamp.

print('Your income is ' + str(income) + ' and you would pay ' + str(lowtaxland_result) + ' income tax in Lowtaxland or ' + str(ripoffland_result) + ' income tax in Ripoffland. You would save ' + str(difference_tax_amount) + ' by paying taxes in Lowtaxland! ')

# This solution uses commas to concatenate.

print('Your income is', str(income), 'and you would pay', str(lowtaxland_result), 
      'income tax in Lowtaxland or', str(ripoffland_result), 'income tax in Ripoffland. You would save', str(difference_tax_amount), 'by paying taxes in Lowtaxland!')


# My answer below passed the test according to Udemy instructor:

income = 250_000
lowtaxland_rate = 0.05 # income tax rate for Lowtaxland
ripoffland_rate = 0.43 # income tax rate for Ripoffland
lowtaxland_result = income * lowtaxland_rate
ripoffland_result = income * ripoffland_rate
difference_tax_amount = ripoffland_result - lowtaxland_result
print('Your income is', str(income), 'and you would pay', str(lowtaxland_result), 
      'income tax in Lowtaxland or', str(ripoffland_result), 'income tax in Ripoffland. You would save', str(difference_tax_amount), 'by paying taxes in Lowtaxland!')


# Solution Answer per Udemy - Here's a sample solution to Coding Exercise 2:

income = 250_000
lowtaxland_rate = 0.05
ripoffland_rate = 0.43

print('Your income is', income, 'and you would pay', income * lowtaxland_rate, 'income tax in Lowtaxland or', income * ripoffland_rate, 
      'income tax in Ripoffland. You would save', income * ripoffland_rate - income * lowtaxland_rate, 'by paying taxes in Lowtaxland!')


# Solution explanation:
# The challenge in this exercise is to be precise and pay attention to all the spaces 
# between all the parts of the final message. 
# We can use commas within a print() statement to that end, just like shown in the hint. 