import sys
import os


# create a class named Product
class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id



    def write_to_file(self):
        path = os.path.join(os.path.dirname(__file__),self.student_id + ".txt")
        open(path, "w").write(self.__str__())

    # summary method
    def __str__(self):
        return f"The student with id of {student_id} is named {last_name}, {first_name}"
try:
    if len(sys.argv) != 4:
        print(f"Usage: {os.path.basename(__file__)} <first_name> <last_name> <student_id>")
        exit()
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    student_id = sys.argv[3]
    student = Student(first_name, last_name, student_id)
    print(student)
    student.write_to_file()
except Exception as e:
    print(e, file=sys.stderr)