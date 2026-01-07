# Types of operators in python

# Arithmetic operators: +, -, *, /, %, **, //
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not
# Assignment operators: =, +=, -=, *=, /=, %=, **=, //= used to assign values to variables.
# Identity operators: is and is not
# Membership operators: in and not in

# Arithmetic operations in python (Integers)

print(1+2)      # addition
print(5-3)      #subtraction
print(2*3)      # multiplication
print(4/2)      # division
print(9%2)      # modulus
print(2**3)     # exponentiation

# Floating numbers

print("pi value:", 3.14)
print("gravity:", 9.81)
print ("light speed:", 3e8)  # 3 x 10^8
print("small number:", 2.5e-4)  # 2.5 x 10^-4

# declaring variables
num_one = 6 
num_two = 4

total = num_one + num_two
diff = num_two - num_one
product = num_one * num_two
div = num_two / num_one
remainder = num_two % num_one

# Printing values with label
print('total: ', total)
print('difference: ', diff)
print('product: ', product)
print('division: ', div)
print('remainder: ', remainder)

# calculating the area of a rectangle
length = 10
width = 16
area_of_rectangle = length * width
print("Area of rectangle: ", area_of_rectangle)

# Calculating a weight of an object
mass = 68
gravity = 9.81
weight = mass * gravity
print("weight:", weight, "N")                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 68 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume 
print("density:", density, "Kg/m^3")                  # Adding unit to the density

# exercises # exercises # exercises # exercises # exercises

# declare your age as integer variable
my_age = 25

# declare your height as a float variable
my_height = 5.5 # in feet. pretty tall huh?

# declare a variable that store a complex number
my_complex_number = 2 + 5j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = 20
height = 10 
area_of_triangle = 0.5 * base * height
print("Area of triangle:", area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle

side_a = 4
side_b = 6
side_c = 5
perimeter_of_triangle = side_a + side_b + side_c 
print("perimeter of triangle:", perimeter_of_triangle)

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

radius = 22
pi = 3.14
area_of_circle = pi * radius *radius
circumference_of_circle = 2 * pi * radius
print("area of circle:", area_of_circle)
print("circumference of circle:" ,circumference_of_circle)

len("Python")
len("dragon")
print(len("python") != len("dragon"))
print('on' in 'python' and 'on' in 'dragon')

int("9.8") == 10   # False. 9.8 is float not integer

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

working_hours = int(input("Enter your working hours: "))
hourly_rate = int(input("Enter your hourly rate: "))
name = input("Enter your name: ")

weekly_earning = working_hours * hourly_rate

output = "Hello " + name + ", your weekly earning is: " + str(weekly_earning)
print(output)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

years = int(input("enter number of years you have lived: "))
seconds = years * 365 * 24 * 60 * 60
print("You have lived for", seconds, "seconds.")   

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

for i in range(1, 6):
    print(i, 1, i, i**2, i**3)