height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2
print(f'Your BMI is {bmi}')

if BMI < 18.5:
    print("You are underweight.")
elif BMI <= 24.9:
    print("You are healthy.")
elif BMI <= 29.9:
    print("You are over weight.")
else
    print("You are obese.")
