list1 = ["banana", "appple", "strawberry","cherry"]
list2 = [1,2,3,4]
set1 = set(list1 + list2)
print(f"before add: {set1}")
set1.add(5)
print(f"after add: {set1}")
set1.remove("strawberry")
print(f"after remove: {set1}")

set2 = set(list(set1)[:3])

print(f"difference: {set1.difference(set2)}")

for x in set1.union(set2):
    print(f"Values are: ",x)