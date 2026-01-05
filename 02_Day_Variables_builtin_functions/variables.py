# Variables in python. The equal sign used is an assigner and does not represent equality as in mathematics.

first_name = "Moyosore"
last_name = "Afolabi"
country = "Nigeria"
city = "Lagos"
age = "250"
is_married = "false"
skills = ["HTML", "Python", "CSS"]

person_info = {
    "firstname" : "Moyosore",
    "last_name" : "Afolabi",
    "country": "Nigeria",
    "city": "Lagos"
}


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

# Declaring multiple variables in one line
first_name , last_name, country, age, is_married = "Moyosore", "Afolabi", "Nigeria", 250, False

print(first_name, last_name, country, age, is_married)

# Different data types in python
first_name = "Moyosore"
last_name = "Afolabi"
country = "Nigeria"
city = "Lagos"
age = "250"

# Printing the data types of the variables
print(type('Moyosore'))          # str
print(type(first_name))          # str
print(type(10))                  # int
print(type(3.14))                # float
print(type(1 + 1j))              # complex
print(type(True))                # bool
print(type([1, 2, 3, 4]))        # list
print(type({'name':'Moyosore'})) # dict
print(type((1,2)))               # tuple
print(type(zip([1,2],[3,4])))    # zip

# Exercise : Arithmetic operations

num_one = 5
num_two = 4
num_one + num_two == 9
num_one - num_two == 1
num_one * num_two == 20
num_one / num_two == 1.25
num_one % num_two == 1
num_one ** num_two == 625