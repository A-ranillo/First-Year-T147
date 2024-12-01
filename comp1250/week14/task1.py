# 101475343
# philip bezalel asher ranillo

import os

def get_filename(filename):
    if not "." in filename:
        filename += ".txt"
        print(filename)

    #filename exist or not
    if os.path.exists(filename):
        raise FileExistsError("File Already exists")
    return filename
def create_file(filename):
    with open(filename, "w"):
        print("File Created")

def get_content():
    content = input("Enter your content: ")
    if len(content) < 10:
        raise ValueError("Content is too short")
    return content

def add_content(filename, content):
    with open(filename, "a") as file:
        file.write(content+'\n')

try:
    filename = input("Enter filename: ")
    get_filename(filename)
    content = get_content()
    add_content(filename,content)
    print("Data is appended to the file")

except (FileExistsError,ValueError) as Err:
    print("Error", Err)