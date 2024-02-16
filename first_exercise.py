# print("hello " + input("what is your name?"))

# count the total number of character in the string

# def count_character_in_str(str):
#     count = 0    
#     i = 0
#     for i in str:
#         i =+ 1
#         count = count + i
#     print("the number of charecter in the given str is :", count)
#     return count
# count_character_in_str("ali")

# 2 example count the number of each character in the string

# def count_characters(s):
#     char_count = {} # this create an empty dictionary to store character counts
#     for char in s:
#         if char in char_count:
#             char_count[char] += 1
#         else:
#             char_count[char] = 1
#     return char_count

# input_string = "hello world"
# result = count_characters(input_string)
# print(result)

print("the number of character is: ", len(input("enter the name?")))