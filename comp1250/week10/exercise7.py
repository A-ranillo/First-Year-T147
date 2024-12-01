import re
# """
# Write a function that
#     -takes 3 parameters
#     -returns a list of the data types of the arguments as strings. Example: task1(1, "hi", 1.1) -> ['int', 'string', 'float']
# -Call and output the result of the function above with 1 string, 1 integer & one float data type
# -Call and output the result of the function above with all numerical data types
# -Call and output the result of the function above with all string data types
# """

print(f"Task 1: ")

def task1(arg1, arg2, arg3):
    return type(arg1).__name__, type(arg2).__name__, type(arg3).__name__

print("Case 1: ",task1(1, "hi", 1.1))
print("Case 2: ",task1(1, 2, 3))
print("Case 3: ",task1("hi", "hello", "world"))


print("Task 2")
# """
# Write a function that
#     -takes 2 parameters
#         -the first parameter is a string
#         -the second parameter is a number
#             -verify that both parameters are the specified data types 
#             -verify that the number has a value of at least 2
#                 -if the above verifications fail, return False
#                 -if not, return a string that repeats the text X times (value of the second argument)
# -Call and output the result of the function above with values of Hello and -2
# -Call and output the result of the function above with values of World and 5
# -Call and output the result of the function above with any two values that will return False
# -Call and output the result of the function above with any two values that will return a string 
# """

def task2(text, num):
    if not isinstance(text, str) or not isinstance(num, int) or num < 2:
        return False
    else:
        return text * num

print("Case 1: ", task2("Hello", -2))
print("Case 2: ", task2("World", 5))
print("Case 3: ", task2("World", "5"))
print("Case 4: ", task2(1, 1))

print("Task 3: ")
# """Write a function that
#     -takes no arguments
#     -outputs your first name
#     -returns your last name
# """
def task3():
    print("Philip Bezalel Asher")
    return "Last Name: Ranillo"

print("Case 1:", task3())

print("task 4: ")
# """Write a function that
#     -takes no arguments
#     -outputs your first name
#     -returns your last name
# """
def task4(num1, num2):
    if num1%num2 ==0:
        return True
    else:
        return False
print("Case 1: ", task4(15,5))

print("Task 5 ")
#Write a function that will determine if a text is a valid Canadian postal code. It will return True or False
def task5(postal_code):
    pattern = r'^[a-zA-Z][0-9][a-zA-Z] [0-9][a-zA-Z][0-9]$'
    if re.match(pattern, postal_code):
        return True
    return False
print("Case 1:", task5("abc"))

#Write a function that, given a first and last name, will return a text in the format of "lastname, firstname"
print("task6")

def task6(first_name, last_name):
    return last_name + "," + first_name

print("Case 1: ", task6("Philip Bezalel Asher", "Ranillo"))

print("Task 7: 1 to 6")
# """
# Task 6:formatting name
# Task 5:check if the input is a correct canadian postal code
# Task 4:determine if number is a factor of another number
# Task 3:print name
# Task 2:checking if the input arguments are integers or strings
# Task 1:printing out what kind of data types of the argument
# """

