def student_info(student_no, first_name, last_name):
    print(student_no, first_name, last_name)
    filename = f"student{student_no}.txt"
    with open(filename, "w") as file:
        file.write(f"{first_name} {last_name}")

def main():
    student_no = input("Enter student number: ")
    first_name = input("Please enter first name: ")
    last_name = input("Please enter last name: ")
    student_info(student_no, first_name, last_name)

if __name__ == '__main__':
    main()

