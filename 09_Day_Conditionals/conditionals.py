#  if is used to check if a condition is true and to execute the block code.
a = 5
if a > 0:
    print("A is a positive number")

# if else. If condition is true the first block will be executed, if not the else condition will run.
a = -5
if a > 0:
    print("A is a positive number")
else:
    print("A is not a positive number")

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

# or
a = 3
print('A is positive') if a > 0 else print('A is negative') 

# logical operators
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')

user = 'Phenomenal_Mo'
access_level = 5
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

# exercises

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

a = int(input("enter a number:"))
b= int(input("enter another number:"))
if a > b:
     print("a is greater than b")
elif a < b:
     print("a is smaller than b")
else:
     print("a is equal to b")
     

grade = int(input("Enter your score: "))

if 90 <= grade <= 100:
    print("Your grade is A")
elif 80 <= grade <= 89:
    print("Your grade is B")
elif 70 <= grade <= 79:
    print("Your grade is C")
elif 60 <= grade <= 69:
    print("Your grade is D")
elif 0 <= grade <= 59:
    print("Your grade is F")
else:
    print("Invalid score")


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
