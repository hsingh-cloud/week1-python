# The "if" instruction - conditional statement

user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')

# Note that indentation is very important in Python.
# The code to be executed when and only when the condition is met
# must be indented, either with spaces or with tabulators.
# The recommendation is to always use exactly four spaces as the 
# indentation.

# Note that you can also execute more than one instruction when the 
# condition is met.

user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')

# These two print invocations constitute the same block.
# All instructions from the same if block must be indented in the same way.


user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
print('Sorry, you do not qualify') # see next note

# removed indentation and this last print function is 
# no longer part of the if block and so python will print it.

user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify') # need to indent to treat as same IF block

user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify')

# in the example below, the IF statement has three scenarios:
# (1) under 30
# (2) exactly 30
# (3) over 30

user_age = int(input('What is your age? '))
if user_age > 30:
    print('You are over 30 years old')
    print('Sorry, you do not qualify')
elif user_age == 30:
    print('You are exactly 30 years old')
    print('You will need to meet additional conditions to qualify')
else:
    print('You are 30 years old or younger')
    print('Congratulations, you qualify')

# if condition_a_met:
#     do_scenario_a ()
# elif condition_b_met:
#     do_scenario_b ()
# elif condition_c_met:
#     do_scenario_c()
# else:
#     do_scenario_d()

