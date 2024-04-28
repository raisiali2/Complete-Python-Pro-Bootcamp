print("enter your height in meters e.g., 1.55")
height = float(input())

print("enter your weight in kilograme e.g., 72")
weight = int(input())

bmi = weight / (height * height)

if bmi < 18.5:
    print("under weight")
    
elif bmi < 25:
    print("normal weight")
    
elif bmi < 30:
    print("slightly over weight")
    
elif bmi < 35:
    print("obese")
    
else:
    print("clinically obese")
    