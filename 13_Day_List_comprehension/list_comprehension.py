# List comprehension in Python is a compact way of creating a list from a sequence. 
# It is a short way to create a new list

# One way
language = 'Python'
lst = list(language) # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# generating numbers
numbers = [i for i in range(11)]
print(numbers)

squares = [i * i for i in range(11)]
print(squares)

numbers = [(i, i * i) for i in range(11)]
print(numbers)

even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

odd_numbers = [i for i in range(21) if i % 2 != 0]
print(odd_numbers)

# lambda function

add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))

# OR

print((lambda a, b: a + b)(2, 3))

square = lambda x: x ** 2
print(square(9))

cube = lambda x : x ** 3
print(cube(5))

multiple_variables = lambda a, b, c : a **2 + b +8 % c ** 3
print(multiple_variables(6, 8, 3))

# exercises

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
positive_numbers = [i for i in numbers if i > 0]
print(positive_numbers)

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_list = [letters for row in countries for letters in row]
print(flattened_list)

countries_dicts = []

for item in countries:
    country, city = item[0]
    countries_dicts.append({
        'country': country,
        'city': city
    })

print(countries_dicts)
