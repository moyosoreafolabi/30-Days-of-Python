# A function is a reusable block of code or programming statements designed to perform a certain task

def generate_full_name ():
    first_name = 'Moyosore'
    last_name = 'Afolabi'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

# functions with single parameters
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Moyosore'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# functions with two parameters

def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Moyosore','Afolabi'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age 

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # the value has to be changed to a string first
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))

# passing arguments with key and value

def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Moyosore', lastname = 'Afolabi')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # Order does not matter 

# functions returning a string value

def print_name(firstname):
    return firstname
print_name("Moyosore")

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname + space + lastname
    return full_name
print_full_name(firstname= "Moyosore", lastname = "Afolabi")


# exercises
def add_two_numbers(a, b):
    return a + b

import math

def area_of_circle(r):
    return math.pi * r * r

def add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return "Error: all arguments must be numbers"
        total += num
    return total

def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

import math

def solve_quadratic_eqn(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (x1, x2)

    elif discriminant == 0:
        x = -b / (2*a)
        return (x,)

    else:
        return "No real solutions"

def print_list(lst):
    for item in lst:
        print(item)

def capitalize_list_items(items):
    capitalized_items = []
    for item in items:
        capitalized_items.append(item.capitalize())
    return capitalized_items

def factorial(n):
    if n < 0:
        return "Error: factorial is not defined for negative numbers"
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def greet(name="Guest"):
    print(f"Hello, {name}!")

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
