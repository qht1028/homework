#!/usr/bin/env python3

import sys
import random
import math
# Question 1: Life or "Dice"
"""
trial = 10000
for dc in range(1,21): 
    nor = 0
    adv = 0
    dis = 0
    for i in range(trial):
        d1 = random.randint(1,20)
        d2 = random.randint(1,20)
        if d1 >= dc: 
            nor += 1
        if max(d1,d2) >= dc: 
            adv += 1
        if min(d1,d2) >= dc: 
            dis += 1
    print(f'{dc}\t{nor/trial:.3f}\t{adv/trial:.3f}\t{dis/trial:.3f}')
"""
# Question 2: Death and "Dice"
'''
trial = 10000
survive = 0
death = 0
stable = 0
for i in range(trial): 
    fail = 0
    success = 0 
    while True:
        dc = random.randint(1,20)
        if dc == 20: 
            survive += 1
            break
        elif dc >= 10: 
            success += 1
        elif dc > 1: 
            fail += 1
        elif dc == 1: 
            fail += 2
        if fail >= 3 or success == 3: 
            break
    if success > 2: 
        stable += 1
    elif fail > 2: 
        death += 1
print("Survival rate: " f'{survive/trial:.3f}')
print("Stablized rate: " f'{stable/trial:.3f}')
print("Death rate: " f'{death/trial:.3f}')
'''
# Question 3: Lucky Haflings
"""
trial = 10000
survive = 0
death = 0
stable = 0
for i in range(trial): 
    fail = 0
    success = 0 
    while True:
        dc = random.randint(1,20)
        if dc == 1: 
            dc = random.randint(1,20)
        if dc == 20: 
            survive += 1
            break
        elif dc >= 10: 
            success += 1
        elif dc > 1: 
            fail += 1
        elif dc == 1: 
           fail += 2
        if fail >= 3 or success >= 3: 
            break
    if success > 2: 
        stable += 1
    elif fail > 2: 
        death += 1
print(death, stable, survive)
print("Survival rate: " f'{survive/trial:.3f}')
print("Stablized rate: " f'{stable/trial:.3f}')
print("Death rate: " f'{death/trial:.3f}')
"""
# Extra Question: Blessed by God
"""
trial = 10000
survive = 0
death = 0
stable = 0
for i in range(trial): 
    fail = 0
    success = 0 
    while True:
        dc = max(random.randint(1,20), random.randint(1,20))
        if dc == 20: 
            survive += 1
            break
        elif dc >= 10: 
            success += 1
        elif dc > 1: 
            fail += 1
        elif dc == 1: 
           fail += 2
        if fail >= 3 or success >= 3: 
            break
    if success > 2: 
        stable += 1
    elif fail > 2: 
        death += 1
print(death, stable, survive)
print("Survival rate: " f'{survive/trial:.3f}')
print("Stablized rate: " f'{stable/trial:.3f}')
print("Death rate: " f'{death/trial:.3f}')
"""
# Question 4: A Rookie Speller
"""
normal = 0
adept = 0
trial = 10000
for i in range(trial): 
    damage = random.randint(1,10)
    normal += damage
    if damage == 1: 
        damage += 1
        adept += damage
    else: 
        adept += damage
print("Normal average: " f'{normal/trial:.3f}')
print("Adept average: " f'{adept/trial:.3f}')
print("Damage difference: " f'{adept/trial-normal/trial:.3f}')
"""
# Question 5: Careless Piercer
"""
trial = 10000
me = 0
Jorg = 0
Gastin = 0
for i in range(trial): 
    roll = random.randint(1,8)
    if roll <= 3: 
        roll3 = random.randint(1,8)
        me += roll3
        Jorg += roll3
        Gastin += roll3
    elif roll <= 4 : 
        roll1 = random.randint(1,8)
        me += roll1
        Jorg += roll
        Gastin += roll
    elif roll <= 6: 
        roll2 = random.randint(1,8)
        me += roll 
        Jorg += roll2
        Gastin += roll
    else: 
        me += roll 
        Jorg += roll
        Gastin += roll
print(f'{me/trial:.3f}, {Jorg/trial:.3f},{Gastin/trial:.3f}')
"""
# Question 5: Another Careless Piercer
"""
threshold = 6
for i in range(1, threshold+1): 
    trial = 10000
    normal = 0
    reroll = 0
    for j in range(trial): 
        roll = random.randint(1,8)
        normal += roll
        if roll > i: 
            reroll += roll
        else: 
            roll = random.randint(1,8)
            reroll += roll 
    print(f'{i}\t{normal/trial:.3f}\t{reroll/trial:.3f}')
"""
# Question 6: RMT
"""
for dc in range(1,20): 
    trial = 10000
    normal = 0
    ring = 0
    cloak = 0
    for j in range(trial): 
        d1 = random.randint(1,20)
        d2 = random.randint(1,20)
        if d1 >= dc: 
            normal += 1
        if d1 + 5 >= dc: 
            ring += 1
        if max(d1, d2) >= dc: 
            cloak += 1
    print(f'{dc}\t{normal/trial:.3f}\t{ring/trial:.3f}\t{cloak/trial:.3f}')
"""