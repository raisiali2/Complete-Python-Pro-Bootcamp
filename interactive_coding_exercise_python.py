# there are two variables, a and b from input 
a = input("input a: ")
b = input("input b: ")

# my code to switch the values of variables
# need for temporary store that keep value of a which change in the next step
# then we use this temporary store that has value of a before change, give to b.
c = a
a = b
b = c

print("a:" + a)
print("b:" + b)

# next do the same exercise for string value

a = input("enter string: ")
b = input("enter string:")

# solution
c = a
a = b
b = c

print("a:" + a)
print("b:" + b)
