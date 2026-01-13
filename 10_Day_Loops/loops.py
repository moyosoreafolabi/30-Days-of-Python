# Loops are used to handle repetitive task programming languages
# while loop is used to execute a block of statements repeatedly until a given condition is satisfied.

count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4

count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)

count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break

count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1

# for loop
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)       

language = 'Python'
for letter in language:
    print(letter)

# or

for i in range(len(language)):
    print(language[i])

number = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

person = {
    "first_name" : "Moyosore",
    "last_name": "Afolabi",
    "age":250,
    "country":"Nigeria",
    "is_marred": False,
    "skills":['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    "address":{
        "street":"Noneya island",
        "zipcode":"0221"
    }
    }

for key in person:
    print(key)

for key, value in person.items():
    print(key, value)

it_companies = {"facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"}
for company in it_companies:
    print(company)

numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break       # the loop stops at 3

numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
    if number == 3:
        continue
print("next number should be ", number + 1) if number !=5 else print("loop's end")

lst = list(range(11))
print(lst)
st = set(range(1, 11))
print(st)

lst = list(range(0,11,2))
print(lst)

person = {
    "first_name" : "Moyosore",
    "last_name": "Afolabi",
    "age":250,
    "country":"Nigeria",
    "is_marred": False,
    "skills":['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    "address":{
        "street":"Noneya island",
        "zipcode":"0221"
    }
    }

for key in person:
    if key == "skills":
        for skill in person["skills"]:
            print(skill)

for number in range(11):
    print(number)  
else:
    print('The loop stops at', number)

for number in range(6):
    pass

# exercises

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