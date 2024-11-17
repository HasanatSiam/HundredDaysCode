print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12 or 15? "))
percentage = tip/100
total_tips = bill * percentage
total_bill = bill + total_tips
person = int(input("How many people to split the bill? "))
print(F"Each person should pay: ${round(total_bill/person, 2)}")