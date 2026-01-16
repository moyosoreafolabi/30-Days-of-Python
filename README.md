# 🐍 30 Days of Python - Learning Log

Welcome to my repository for the **30 Days of Python** challenge! I am documenting my learning journey, code snippets, and solutions to the daily exercises here.

## 📅 Progress Tracker

| Day | Topic | Status |
|:---:|:---|:---:|
| **01** | **Introduction, Data Types, Comments** | ✅ |
| **02** | **Variables, Built-in Functions** | ✅ |
| **03** | **Operators** | ✅ |
| **04** | **Strings** |✅  |
| **05** | **Lists** |✅  |
| **06** | **Tuples** |✅  |
| **07** | **Sets** | ✅ |
| **08** | **Dictionaries** | ✅ |
| **09** | **Conditionals** | ✅  |
| **10** | **Loops** | ✅ |
| **11** | **Functions** |✅  |
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

### Day 4: Strings
**Topics Covered:**

- Creating a String
- String Concatenation
- Escape Sequences in Strings
- String formatting
- Python Strings as Sequences of Characters
- String Methods

**Code Snippet:**
```python
result = "Thirty" + ' ' + "Days" + ' ' + "Of" + ' ' + "Python"
print(result)

result_two = "Coding" + " " + "For" + " " + "All"
print(result_two)

company = "coding for all"
print(company)
print(len(company))             # checks length of string
print(company.upper())          # changes string to uppercase
print(company.lower())          # changes string to lowercase

company = "Coding For All"
first_word = company.split()[2]
print(first_word)

company = "coding for all"
print(company.find("coding"))

print(company.replace("coding", "Python"))     # replaces coding with python in the variable "company"

statement = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
print(statement.index(sub_string))          # prints first occurence of because
print(statement.rindex(sub_string))         # prints last occurence of because

statement = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
print(statement.strip(sub_string))          # removes because from string


print("Name\tAge\tCountry\tCity")           # tab spaces
print("Moyosore\t25\tNigeria\tLagos")       # tab spaces

print("I am enjoying learning Python.\nI hope you are enjoying it too.")   # shifts second sentence to the next line
print("I am enjoying this challenge.\nI just wonder what is next.")        # likewisw

radius = 10 
area = 3.14 * radius ** 2 
result = print(area)
print("The area of a circle with radius 10 is :", area)

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " ".join(libraries)                # Returns a concatenated string
print(result)
```

### Day 5: Lists
**Topics Covered:**

- How to Create a List
- Accessing List Items Using Positive Indexing
- Accessing List Items Using Negative Indexing
- Unpacking List Items
- Slicing Items from a List
- Modifying Lists
- Checking Items in a List
- Adding Items to a List
- Inserting Items into a List
- Removing Items from a List
- Removing Items Using Pop
- Removing Items Using Del
- Clearing List Items
- Copying a List
- Joining Lists
- Counting Items in a List
- Finding Index of an Item
- Reversing a List
- Sorting List Items

**Code Snippet:**
```python

days = []
print(days)

months = ["january", "february", "march", "april", "may", "june"]
print(len(months))
first_item = months[0]
middle_item = months[3]
last_item = months[5]
print(first_item , middle_item , last_item)

mixed_data_types = ["moyosore", "25", "5.5 inches", "engaged", "lagos"]
print(mixed_data_types)

it_companies = ["facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"]
print(it_companies)
print(len(it_companies))
it_companies[0] = "instagram"
print(it_companies)

it_companies.append("telegram")
print(it_companies)

it_companies.insert(3, "chatgpt")
print(it_companies)

does_exist= "instagram" in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)

it_companies.pop(0)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

del it_companies
# print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack.insert(5, "Python")
print(full_stack)
full_stack.insert(6, "SQL")
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(min_age)
print(max_age)

ages.append(min_age)
ages.append(max_age)
ages.sort()
print(ages)

average = sum(ages) / len(ages)
print(average)

age_range = max_age - min_age
print(age_range)

min_diff = abs(min_age - average)
max_diff = abs(max_age - average)
print(min_diff)
print(max_diff)
```

### Day 6: Tuples
**Topics Covered:**

- Creating a Tuple
- Tuple length
- Accessing Tuple Items
- Slicing tuples
- Changing Tuples to Lists
- Checking an Item in a Tuple
- Joining Tuples
- Deleting Tuples

**Code Snippet:**
```python

empty_tuple = ()
sibs = ("Doyin", "Dayo", "Tunde", "Damola")
print(sibs)
print(len(sibs))   
family_members = list(sibs)
family_members[0] = "kehinde"
family_members[1] = "joseph"
print(family_members)

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ("milk", "cheese", "meat", "bacon")
food_stuff = fruits + vegetables + animal_products
print(animal_products)

# Print the lists and it length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Food stuff:', food_stuff)
print('Number of food items:', len(food_stuff))


food_stuff_lt = list(food_stuff)
print(food_stuff_lt)

item = food_stuff[2]
print(item)

del food_stuff
print(food_stuff)  # this will raise an error since food_stuff has been deleted
```

### Day 7: Sets
**Topics Covered:**

- Creating a Set
- Getting Set's Length
- Accessing Items in a Set
- Checking an Item
- Adding Items to a Set
- Removing Items from a Set
- Clearing Items in a Set
- Deleting a Set
- Converting List to Set
- Joining Sets
- Finding Intersection Items
- Checking Subset and Super Set
- Checking the Difference Between Two Sets
- Finding Symmetric Difference Between Two Sets
- Joining Sets

**Code Snippet:**
```python

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'} 
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

it_companies = {"facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"}
print(len(it_companies))
it_companies.add("twitter")
print(it_companies)

extra_companies = {"whatsapp", "apple", "netflix"}
it_companies.update(extra_companies)
print(it_companies)

it_companies.remove("whatsapp")
print(it_companies)
```

### Day 8: Dictionaries
**Topics Covered:**

- Creating a Dictionary
- Dictionary Length
- Accessing Dictionary Items
- Adding Items to a Dictionary
- Modifying Items in a Dictionary
- Checking Keys in a Dictionary
- Removing Key and Value Pairs from a Dictionary
- Changing Dictionary to a List of Items
- Clearing a Dictionary
- Deleting a Dictionary
- Copy a Dictionary
- Getting Dictionary Keys as a List
- Getting Dictionary Values as a List

**Code Snippet:**
```python

student = {
        "first_name":"Paige",
        "last_name":"Greene",
        "gender":"female",
        "age":22,
        "marital status":"single",
        "skills":["guitar", "singing", "reading"],
        "country":"America",
        "city":"Louisiana",
        "address":"nyu",
          
        }

print(student)
print(len(student))
print(student["skills"])

student["skills"].append("driving")
print(student)

keys = student.keys()
print(keys)

values = student.values()
print(values)

print(student.items())
print(student)

print(student.pop("last_name"))
print(student.clear())
```

### Day 9: Conditionals
**Topics Covered:**

- If Condition
- If Else
- If Elif Else
- Short Hand
- Nested Conditions
- If Condition and Logical Operators
- If and Or Logical Operators

**Code Snippet:**
```python

age = int(input("enter your age:"))
if age >= 18: 
    print("You are old enough to drive")
else:
     print("You need 3 more years to learn to drive")

my_age = int(input("enter your age:"))
your_age = int(input("enter your age:"))
if my_age > your_age:
    print("I am older than you")
elif my_age < your_age:
     print("You appear to be older. my bad")
else:
     print("we are age mates!")


month = input("Enter the month you are in: ").lower()

if month in ("september", "october", "november"):
    print("The season is autumn")
elif month in ("december", "january", "february"):
    print("The season is winter")
elif month in ("march", "april", "may"):
    print("The season is spring")
elif month in ("june", "july", "august"):
    print("The season is summer")
else:
    print("Invalid month")
```
### Day 10: Loops
**Topics Covered:**

- While Loop
- Break and Continue - Part 1
- For Loop
- Break and Continue - Part 2
- The Range Function
- Nested For Loop
- For Else
- Pass

**Code Snippet:**
```python

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number)

lst = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for lst in lst:
    print(lst)

total = 0

for i in range(101):  # 0 to 100 inclusive
    total += i

print("The sum of all numbers from 0 to 100 is:", total)

sum_even = 0
sum_odd = 0

for i in range(101):  # 0 to 100
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i

print("Sum of all even numbers from 0 to 100:", sum_even)
print("Sum of all odd numbers from 0 to 100:", sum_odd)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for fruit in fruits:
    reversed_fruits.insert(0, fruit)

print(reversed_fruits)
```

### Day 11: Functions
**Topics Covered:**

- Defining a Function
- Declaring and Calling a Function
- Function without Parameters
- Function Returning a Value - Part 1
- Function with Parameters
- Passing Arguments with Key and Value
- Function Returning a Value - Part 2
- Function with Default Parameters
- Arbitrary Number of Arguments
- Default and Arbitrary Number of Parameters in Functions
- Function as a Parameter of Another Function

**Code Snippet:**
```python

ef add_all_nums(*nums):
    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return "Error: all arguments must be numbers"
        total += num
    return total

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
```
## 🛠️ Setup & Running

To run the code for a specific day:

1. Navigate to the day's folder (e.g., `cd Day_01`)
2. Run the python file:
   ```bash
   python3 helloworld.py
   
## 📚 Resources
- [Official 30 Days of Python Repo](https://github.com/Asabeneh/30-Days-Of-Python)

