#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:33:57 2021

@author: user
"""

# Ask user for name

name = input("What is your name?: ")

# Ask user for age

age= input("How old are you?: ")

# Ask user city 

city = input("What city do you live in?: ")


# Ask user what they enjoy

enjoy = input("What do you enjoy doing?: ")


# Create output text

string ="Your name is {} and you are {} years old. You live in {} and you enjoy {}"
output = string.format(name,age,city,enjoy)

print(output)