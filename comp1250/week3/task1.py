user_no = input("Enter a number: ")
res = user_no.isdigit()
if res:
    print(f"{res}, The character {user_no} is numeric")
else:
    print(f"{res}, The character {user_no} is not numeric")
