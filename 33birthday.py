#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

trial=10000
people=23
share=0
for i in range(trial): 
    calendar = [0]*365
    count = 0
    for j in range(people): 
        birthday=random.randint(0,364)
        calendar[birthday] += 1
    for j in range(365): 
        if count < calendar[j]: 
            count = calendar[j]
    if count >= 2: 
        share += 1
print(share/trial)
        

"""
python3 33birthday.py
0.571
"""

