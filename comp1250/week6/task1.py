set1 = set(range(10,21))
set2 = set(range(5,16))
print(f"difference: {set1.difference(set2)}")
print(f"common: {set1.intersection(set2)}")

for x in set1:
    print(f"set1 {x}")

for y in set2:
    print(f"set2 {y}")

