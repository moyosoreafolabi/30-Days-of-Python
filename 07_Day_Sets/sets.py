# a set is used to store unique items

st = set()          # empty set

fruits = {"banana", "orange", "mango", "lemon"}
print(fruits)
print(len(fruits))
print("mango" in fruits)        # true
print("avocado" in fruits)      # false

fruits = {"banana", "orange", "mango", "lemon"}
fruits.add("apple")
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
vegetables = ("tomato", "potato", "cabbage","onion", "carrot")
fruits.update(vegetables)       # allows to add multiple items to a set
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
fruits.remove("banana")
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
fruits.pop()            # removes a random item from the set
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
fruits.clear()      # empties the set
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
del fruits

fruits = ["banana", "mango", "orange", "lemon"]
fruits = set(fruits)        # converts list to set
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
fruits = list(fruits)
print(fruits)

fruits = {"banana", "orange", "mango", "lemon"}
vegetables = {"tomato", "potato", "cabbage","onion", "carrot"}
print(fruits.union(vegetables))     # joins the set

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # Intersection returns a set of items which are in both the sets.

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False

even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'} 
dragon.difference(python)     # {'d', 'r', 'a', 'g'}

# exercises

it_companies = {"facebook", "google", "microsoft", "apple", "IBM", "oracle", "amazon"}
print(len(it_companies))
it_companies.add("twitter")
print(it_companies)

extra_companies = {"whatsapp", "apple", "netflix"}
it_companies.update(extra_companies)
print(it_companies)

it_companies.remove("whatsapp")
print(it_companies)
