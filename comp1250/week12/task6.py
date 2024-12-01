import os

def search_student(field, value):
    if field == 'student number':
        if os.path.exists(f"{value}.txt"):
            with open(f"{value}.txt", 'r') as file:
                first_name = file.readline().strip()
                last_name = file.readline().strip()
                print("Success, Student is found")
                print(f"{first_name} {last_name}")
        else:
            print("Sorry, Student is not found")

def main():
    field = input("Enter the field you want to search: ")
    value = input("Enter the value you have to search: ")
    search_student(field, value)


if __name__ == '__main__':
    main()