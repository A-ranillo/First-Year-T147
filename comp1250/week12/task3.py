import csv

def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "First Name", "Last Name", "Age"])
        for row in data:
            writer.writerow(row)


rows = [
    ["uname1", "Philip", "Ranillo", "100"],
    ["uname2", "John", "Smith", "100"],
    ["uname3", "John", "Doe", "100"]
]

write_csv('task3.csv', rows)