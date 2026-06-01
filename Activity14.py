weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in cm: "))

bodymassindex = weight / ((height/100)**2)
print(f"Your BMI is {bodymassindex}.")

if bodymassindex < 18.5:
    print("Underweight")
elif bodymassindex >= 18.5 and bodymassindex < 25:
    print("Normal")
elif bodymassindex >= 25 and bodymassindex < 30:
    print("Overweight")
else:
    print("Obese")