
weight = float(input("Enter Your Weight (in kilograms): "))
height = float(input("Enter Your Height (in meters): "))

bmi = (weight / (height*height))

if bmi<18.5:
    print("BMI Result: ",bmi)
    print("Under Weight!")
    print("Your need to gain your weight.")

elif 24.9 > bmi > 18.5 or 24.9 == bmi == 18.5:
    print("BMI Result: ",bmi)
    print("Normal Weight!")
    print("You are Perfect.")

elif 29.9 > bmi > 25.0 or 29.9 == bmi == 25.0:
    print("BMI Result: ",bmi)
    print("Over Weight")
    print("You need to lost your weight.")
    print("Perfect BMI is between 18.5 to 24.9.")

elif 34.9 > bmi > 30.0 or 34.9 == bmi == 30.0:
    print("BMI Result: ",bmi)
    print("Obesity Class(I)")
    print("You need to lost your weight.")
    print("Perfect BMI is between 18.5 to 24.9.")

elif 39.9 > bmi > 35.0 or 39.9 == bmi == 35.0:
    print("BMI Result: ",bmi)
    print("Obesity Class(II)")
    print("You need to lost your weight.")
    print("Perfect BMI is between 18.5 to 24.9.")

elif bmi > 40.0:
    print("BMI Result: ",bmi)
    print("Obesity Class(III)")
    print("You need to lost your weight.")
    print("Perfect BMI is between 18.5 to 24.9.")

else:
    print("Try Again...")