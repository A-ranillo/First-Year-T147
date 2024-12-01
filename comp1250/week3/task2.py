user_text = input("Enter an input string: ")
F_user_text = user_text.upper()
print(f"the string with UPPER case is {F_user_text}")
F_user_text = user_text.lower()
print(f"the string with LOWER case is {F_user_text}")
valid_title = user_text.istitle()
if valid_title:
    print(f"The title {valid_title} is valid")
else:
    print(f"the title {valid_title} is not valid")

