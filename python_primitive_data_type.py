# print("hello"[4])

# len(5654)

# num_char = len(input("whqt is you name"))
# new_num_char = str(num_char)
# print("num_char", num_char)


# print(type(new_num_char))

# a = 123
# print(type(a))

# a = str(123)
# print(type(a))39


# number = input("enter you number\n")
# print("entered number is", number)

# print("type of number is: =",type(number))
# num1 = number[0]
# num2 = number[1]
# sum = int(num1) + int(num2)
# print(sum)


# height = input()
# weight = input()

# weight_as_int = int(weight)

# height_as_int = float(height)

# bmi = weight_as_int / height_as_int ** 2

# print("bmi is: ", bmi)

print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("how much tip would you like to give? 10, 12, or 15?"))

people = int(input("how many people to split the bill?"))
bill_with_tip = bill * (1 + tip / 100 )
print(bill_with_tip)

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
final_amount = bill_per_person
print(f"each person should pay: {final_amount:.2f}")