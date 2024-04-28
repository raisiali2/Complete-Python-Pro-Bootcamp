print("enter the year: ")
year = int(input())

if year % 4 == 0:
 if year % 100 == 0:
    print("not a leap year")
    if year % 400 == 0:
        print("year is leap year")
    else:
     print("year is not leap year")
 else:
   print("not a leap year")
else:
  print("not a leap year")