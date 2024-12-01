dict1 = {"a":1,"b":2,"c":3}

print("value of b:", dict1.get("b"))

del dict1["a"]
for key, value in dict1.items():
    print("key and value", key,value)