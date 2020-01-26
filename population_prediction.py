# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 04:07:27 2020

@author: Francis
"""

currentyear_str = input('Enter years')
currentyear_int = int(currentyear_str)

nextyear_str = input('Enter next year')
nextyear_int = int(nextyear_str)

year = nextyear_int - currentyear_int

if (year > 1):
    year = 365 * nextyear_int
else:
    year_str = 365
    
seconds = year * 24*60*60

birth_rate = seconds/7
death_rate = seconds/13
immigrant_rate = seconds/35

current_population = 307357870
estimated_population = float(current_population +birth_rate + immigrant_rate - death_rate)
print(estimated_population)
