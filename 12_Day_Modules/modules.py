# A module is a file containing a set of codes or a set of functions which can be included to an application import mymodule
import mymodule
print(mymodule.generate_full_name("Moyosore", "Afolabi"))


from mymodule import generate_full_name
print(generate_full_name('Moyosore','Afolabi'))

from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       
print(median(ages))     
print(mode(ages))       
print(stdev(ages))  

import math
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

from math import pi     # imports a specific function from the module.
print(pi)

from math import *      # imports all the function in math module.

import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

from random import random, randint      # random module
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive

# exercises

import random

def list_of_hexa_colors(num):
    hex_colors = []
    hex_chars = '0123456789abcdef'

    for _ in range(num):
        color = '#'
        for _ in range(6):
            color += random.choice(hex_chars)
        hex_colors.append(color)

    return hex_colors

import random

def list_of_rgb_colors(num):
    rgb_colors = []

    for _ in range(num):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        rgb_colors.append(f"rgb({r},{g},{b})")

    return rgb_colors

import random

def shuffle_list(lst):
    shuffled = lst[:]          # make a copy so original list is unchanged
    random.shuffle(shuffled)
    return shuffled

import random

def seven_unique_random_numbers():
    return random.sample(range(10), 7)
