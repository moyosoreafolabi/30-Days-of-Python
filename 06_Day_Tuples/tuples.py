# A tuple is a collection of different data types which is ordered and unchangeable (immutable).
# creating a tuple 
empty_tuple = ()
# or 
empty_tuple = tuple()

fruits = ("banana", "orange", "mango", "lemon")
print(len(fruits))

first_fruit = fruits[0]
second_fruit = fruits[1]
last_fruit = fruits[-1]

print(second_fruit)
print(first_fruit)
print(last_fruit)

# changing tuples to lists to make it modifiable

fruits = ("banana", "orange", "mango", "lemon")
fruits = list(fruits)
fruits[0] = "apple"
print(fruits)

fruits = ("banana", "orange", "mango", "lemon")
print("banana" in fruits)       # true
print("avocado" in fruits)      # false

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)

# It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.

fruits = ('banana', 'orange', 'mango', 'lemon')
# del fruits
print(fruits)

# exercises

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