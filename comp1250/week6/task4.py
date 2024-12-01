# Create one list with 3 unique string values
list1 = ["banana", "apple", "bread"]
# Create another list with 3 unique double values
list2 = [1.0,2.0,3.0]
# Create a dictionary where the keys are the string values and the values are the double values
list3 = dict(zip(list1,list2))
print(list3)