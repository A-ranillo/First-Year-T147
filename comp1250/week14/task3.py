# 101475343
# philip bezalel asher ranillo


list = [73, 18, 64, 60, 26, 33, 66, 74, 59, 69, 60, 95, 53, 45, 57, 1, 48, 88, 13, 62]

def task3(list):
    length_list = len(list)
    i = 0
    while i < length_list:
        if list[i] <= 50 and list[i] >= 1:
            with open("50_under.txt", 'a') as file:
                file.write(str(list[i]) + '\n')

        if list[i] <= 100 and list[i] >= 51:
            with open("over_50.txt", 'a') as file:
                file.write(str(list[i]) + '\n')
        i += 1

task3(list)