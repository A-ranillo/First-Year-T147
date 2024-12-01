task1=["two", "hi", "one"]
holder1 = max(task1, key=len)#grabs the first longest string
max_char = len(holder1) #finding character length
control = 0
print ("~~~~~~~~~~~~~~~")
task1.remove(holder1)

while len(max(task1, key=len)) == max_char:
    holder = max(task1, key=len)#grabs the first longest string
    print(task1)
    print(holder)
    task1.remove(holder)
    print(task1)
    holder1 += f"_{holder}"
    print (holder1)
    if not task1:
        break