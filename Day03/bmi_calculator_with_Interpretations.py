height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = weight/(height**2)

if(bmi<18.5):
    print('Underweight')
if(bmi>=18.5 and bmi<25):
    print('Normal weight')
if(bmi>=25):
    print('Overweight')


