height=float(input()) #in meters e.g..158.3
weight=int(input()) #in kg e.g..63
bmi=weight/(height*height) 
if bmi<18.5:
    print(f"your BMI is {bmi}, you are underweight.")
elif bmi<25:
    print(f"your BMI is {bmi}, you are normal weight.")
elif bmi<30:
    print(f"your BMI is {bmi}, you are slightly overweight.")
elif bmi<35:
    print(f"your BMI is {bmi}, you are obese.")
else:
    print(f"your BMI is {bmi}, you are clinically obese.")