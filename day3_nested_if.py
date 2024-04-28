print("nested condition")
height = int(input("enter the height?"))


if height > 120:
    # print("you can ride")
    age = int(input("enter the age?"))
    if age < 12:
        print("pay 5 $")
    elif age <= 18:
        print("pay 7$")
    else:
        print("pay 12$")
  
else:
    print("cant ride")