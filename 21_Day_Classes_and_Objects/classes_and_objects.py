# The class defines attributes and the behavior of the object, while the object, on the other hand, represents the class.
# creating a class

class Person:
    pass
print(Person)

# we create an object by calling the class.

P = Person()
print(P)

class Person:
    def __init__ (self, name):
        self.name = name

p = Person("Moyosore")
print(p.name)
print(p)

class Person:
    def __init__ (self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.country = country
        self.city = city

p = Person("Moyosore", "Afolabi", 25, "Nigeria", "Lagos")
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)

class Person:
    def __init__ (self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

p = Person("Moyosore", "Afolabi", 25, "Nigeria", "Lagos")
print(p.person_info())

class Person:
    def __init__ (self, firstname="Moyosore", lastname="Afolabi", age=25, country="Nigeria", city="Lagos"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.country = country
        self.city = city
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'

p1 = Person()
print(p1.person_info())
p2 = Person("Henry", "Fadeni", 26, "America", "Texas")
print(p2.person_info())

class Person:
    def __init__ (self, firstname="Moyosore", lastname="Afolabi", age=25, country="Nigeria", city="Lagos"):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 
        self.country = country
        self.city = city
        self.skills = []
        
    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. She lives in {self.city}, {self.country}'
    def add_skill(self, skill):
        self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('Henry', 'Fadeni', 26, 'America', 'Texas')
print(p2.person_info())
print(p1.skills)
print(p2.skills)

# inheritance

class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

# exercises

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}   # {description: amount}
        self.expenses = {}  # {description: amount}

    def add_income(self, description, amount):
        if amount < 0:
            raise ValueError("Income amount cannot be negative")
        self.incomes[description] = self.incomes.get(description, 0) + amount

    def add_expense(self, description, amount):
        if amount < 0:
            raise ValueError("Expense amount cannot be negative")
        self.expenses[description] = self.expenses.get(description, 0) + amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        return {
            "Full Name": f"{self.firstname} {self.lastname}",
            "Total Income": self.total_income(),
            "Total Expense": self.total_expense(),
            "Account Balance": self.account_balance(),
            "Incomes": self.incomes,
            "Expenses": self.expenses
        }
