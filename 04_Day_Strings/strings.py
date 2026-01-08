letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be made using a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)

# Multiline string using triple quotes

multiline_string = """I am a student and enjoy learning.
I didn't find anything as rewarding as gaining knowledge.
That is why I decided to try out 30 days of python."""
print(multiline_string)

first_name = "Moyosore"
last_name = "Afolabi"
space = " "
full_name = first_name  +  space + last_name
print(full_name) # Moyosore Afolabi

# Checking the length of a string using len() built-in function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16

# Escape sequence characters 
# \n: new line
# \t: Tab means(8 spaces)
# \\: Back slash
#\': Single quote (')
#\": Double quote (")

print("I am really enjoying this challenge. \nAre you?" )

print("Days\tTopics\tExercises")
print("Day 1\t5\t5")
print("Day 2 \t7\t20")
print("Day 3\t4\t16")
print("Day 4\t1\t32")
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
print('It\'s a beautiful day to learn Python') # to write a single quote inside a single quote

# reversing a string

greeting = "Hello, World!"
print(greeting[::-1])  # !dlroW ,olleH 

# exercises
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.

result = "Thirty" + ' ' + "Days" + ' ' + "Of" + ' ' + "Python"
print(result)

result_two = "Coding" + " " + "For" + " " + "All"
print(result_two)

company = "coding for all"
print(company)
print(len(company))
print(company.upper())
print(company.lower())

company = "Coding For All"
first_word = company.split()[2]
print(first_word)

company = "coding for all"
print(company.find("coding"))

print(company.replace("coding", "Python"))     # replaces coding with python in the variable "company"

statement = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
print(statement.index(sub_string))
print(statement.rindex(sub_string))

statement = "You cannot end a sentence with because because because is a conjunction"
sub_string = "because"
print(statement.strip(sub_string))


print("Name\tAge\tCountry\tCity")
print("Moyosore\t25\tNigeria\tLagos")

print("I am enjoying learning Python.\nI hope you are enjoying it too.")
print("I am enjoying this challenge.\nI just wonder what is next.")

radius = 10 
area = 3.14 * radius ** 2 
result = print(area)
print("The area of a circle with radius 10 is :", area)

libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = " ".join(libraries)                # Returns a concatenated string
print(result)