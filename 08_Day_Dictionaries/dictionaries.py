# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# To create a dictionary we use curly brackets, {} or the dict() built-in function.

empty_dict = {}

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

print(person)
print(len(person))

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

print(person['first_name']) 
print(person['country'])    
print(person['skills'])     
print(person['skills'][0]) 
print(person['address']['street']) 
print(person.get('city'))   # None

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

person["job title"] = "Senior nursing officer"      # adds item to dictionary
person["skills"].append("Baking")
print(person)

person["first_name"] = "Henry"
person["age"] = "26"
print(person)

print("first_name" in person)       # true
print("school" in person)           # false

person.pop("last_name")
person.popitem()        # removes the last item
del person["country"]
print(person)

print(person.items())       # changes dictionary to a list
print(person)

print(person.clear())       # none

del person

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

print(person)
keys = person.keys()
print(keys)

values = person.values()
print(values)

# exercises

dog = {}
dog = {
       "name":"Busta",
       "color":"brown",
       "breed":"boaboel",
       "legs":4,
       "age": 3
       }

print(dog)

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

