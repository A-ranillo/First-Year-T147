list2 = ["apple", "banana", "orange"]
print(list2)
list2.append("strawberry")
print(list2)
list2.remove(list2[0])
print(list2)

print("type a fruit")
fruit = input()

if fruit in list2:
    print("your fruit is in the list!")
    list2.index(fruit)
else:
    print(f"the list only contains {list2}")