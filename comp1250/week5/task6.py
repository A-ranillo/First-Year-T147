user_in1 = int(input("starting num: "))
user_in2 = int(input("ending num: "))
user_in3 = int(input("increment num: "))

for i in range(0,user_in1+1):
    print(f"output1 {i}")

for x in range(1,user_in2+1):
    print(f"output2 {x}")

for y in range(user_in1, user_in2):
    print(f"output3 {y}")

for z in range(user_in1,user_in2,user_in3):
    print(f"output4 {z}")
