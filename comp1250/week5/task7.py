user_in1 = int(input("starting num: "))
user_in2 = int(input("ending num: "))
user_in3 = int(input("increment num: "))

i=0
while i in range(0,user_in1):
    print(f"output1 {i}")
    i = i+1

x=1
while x in range(1,user_in1):
    x = x+1
    print(f"output2 {x}")

y=user_in1
while y in range(user_in1, user_in2):
    y = y+1
    print(f"output3 {y}")

z=user_in1
while z in range(user_in1,user_in2-1,user_in3):
    z = z+user_in3
    print(f"output4 {z}")