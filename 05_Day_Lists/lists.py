# A list is collection of different data types which is ordered and modifiable(mutable). A list can be empty or it may have different data type items.

lst = list()
empty_list = list()
print(len(empty_list))

lst = []                # or we could use square brackets
empty_list = []
print(len(empty_list))

fruits = ["banana", "mango", "orange", "lemon"]
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # list of vegetables
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # list of animal products
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # list of web technologies
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# Print the lists and its length
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))

fruits = ["banana", "mango", "orange", "lemon"]
first_fruit = fruits[0]
print(first_fruit)
last_fruit = fruits[-1]
print(last_fruit)

fruits = ["banana", "mango", "orange", "lemon"]     # modifying lists
fruits[0] = "avocado"
print(fruits)

fruits = ["banana", "mango", "orange", "lemon"]
does_exist = "banana" in fruits         # checking items in a list
print(does_exist)

fruits = ["banana", "mango", "orange", "lemon"]
fruits.append("apple")      # adding items to a list
print(fruits)

fruits.insert(2, "lime")       # insert a single item at a specified index in a list
print(fruits)

fruits = ["banana", "mango", "orange", "lemon"]
fruits.remove("banana")
print(fruits)

fruits.pop(1)
print(fruits)

fruits = ["banana", "mango", "orange", "lemon"]
del fruits[0]
print(fruits)
del fruits[1:3]
print(fruits)
del fruits
# print(fruits) . running this code returns a nameerror as fruits is no longer defined.

fruits = ["banana", "mango", "orange", "lemon"]
fruits.clear()
print(fruits)

fruits = ["banana", "mango", "orange", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)

# joining lists

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

fruits = ["banana", "mango", "orange", "lemon"]
print(fruits.count("orange"))           # 1
print(fruits.index("orange"))

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))       # 3
print(ages.index(24))

fruits = ["banana", "mango", "orange", "lemon"]
fruits.reverse()        # reverses the order of the list
print(fruits)

fruits = ["banana", "mango", "orange", "lemon"]
fruits.sort()       # sorts in alphabetical order
print(fruits)
fruits.sort(reverse=True)       # sorts in descending order
print(fruits)

##exercises

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