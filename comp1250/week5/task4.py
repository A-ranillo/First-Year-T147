list4 = []

for x in range(5,0,-1):
    user = input("Give me a string or variable: ")
    if not user in list4:
        list4.append(user)
    else:
        print(f"thats already in the list you have {x-1} tries left")