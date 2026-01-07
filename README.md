# 🐍 30 Days of Python - Learning Log

Welcome to my repository for the **30 Days of Python** challenge! I am documenting my learning journey, code snippets, and solutions to the daily exercises here.

## 📅 Progress Tracker

| Day | Topic | Status |
|:---:|:---|:---:|
| **01** | **Introduction, Data Types, Comments** | ✅ |
| **02** | **Variables, Built-in Functions** | ✅ |
| 03 | Operators | ⬜ |
| 04 | Strings | ⬜ |
| 05 | Lists | ⬜ |
| 06 | Tuples | ⬜ |
| 07 | Sets | ⬜ |
| 08 | Dictionaries | ⬜ |
| 09 | Conditionals | ⬜ |
| 10 | Loops | ⬜ |
| 11 | Functions | ⬜ |
| 12 | Modules | ⬜ |
| 13 | List Comprehension | ⬜ |
| 14 | Higher Order Functions | ⬜ |
| 15 | Python Type Errors | ⬜ |
| 16 | Python Date time | ⬜ |
| 17 | Exception Handling | ⬜ |
| 18 | Regular Expressions | ⬜ |
| 19 | File Handling | ⬜ |
| 20 | Python Package Manager (PIP) | ⬜ |
| 21 | Classes and Objects | ⬜ |
| 22 | Web Scraping | ⬜ |
| 23 | Virtual Environment | ⬜ |
| 24 | Statistics | ⬜ |
| 25 | Pandas | ⬜ |
| 26 | Python for Web (Flask/Django) | ⬜ |
| 27 | Python with MongoDB | ⬜ |
| 28 | API | ⬜ |
| 29 | Building API | ⬜ |
| 30 | Conclusion | ⬜ |

## 📝 Daily Notes

### Day 1: Introduction

**Topics Covered:**
- Checking python version: `python --version`
- Basic arithmetic operations (`+`, `-`, `*`, `/`, `**`, `%`, `//`)
- Data types:
    - `int` (Integers)
    - `float` (Floating point numbers)
    - `complex` (Complex numbers)
    - `str` (Strings)
    - `bool` (Booleans)
    - `list`, `tuple`, `set`, `dict`
- Checking data types with `type()`

**Code Snippet:**
```python
# Checking data types
print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name': 'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
```

### Day 2: Variables
**Topics Covered:**
- assigning variables 
- printing values stored in the variables 
- declaring multiple variables in one line
- different data types
- arithmetic operations 

**Code Snippet:**
```python
# Printing the values stored in the variables

print("First name", first_name)
print("First name lenghth", len(first_name))
print("Last name: ", len(last_name))
print("Country: ", country)
print("City: ",city)
print("Age: ", age)
print("Married:", False)
print("Skills: ", skills)
print("Person information: ", person_info)
```

### Day 3: Variables
**Topics Covered:**

- Boolean
- Operators
- Assignment Operators
- Arithmetic Operators:
- Comparison Operators
- Logical Operators 

**Code Snippet:**    **Code for exercises:**
```python

# calculating the area of a rectangle
length = 10
width = 16
area_of_rectangle = length * width
print("Area of rectangle: ", area_of_rectangle)

# Calculating a weight of an object
mass = 68
gravity = 9.81
weight = mass * gravity
print("weight:", weight, "N")                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 68 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume 
print("density:", density, "Kg/m^3")                  

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

working_hours = int(input("Enter your working hours: "))
hourly_rate = int(input("Enter your hourly rate: "))
name = input("Enter your name: ")

weekly_earning = working_hours * hourly_rate

output = "Hello " + name + ", your weekly earning is: " + str(weekly_earning)
print(output)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")   

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
```

## 🛠️ Setup & Running

To run the code for a specific day:

1. Navigate to the day's folder (e.g., `cd Day_01`)
2. Run the python file:
   ```bash
   python3 helloworld.py
   
## 📚 Resources
- [Official 30 Days of Python Repo](https://github.com/Asabeneh/30-Days-Of-Python)

