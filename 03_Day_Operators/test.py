working_hours = int(input("Enter your working hours: "))
hourly_rate = int(input("Enter your hourly rate: "))
name = input("Enter your name: ")

weekly_earning = working_hours * hourly_rate

output = "Hello " + name + ", your weekly earning is: " + str(weekly_earning)
print(output)
