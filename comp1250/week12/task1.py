def write_file(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line + '\n')
            
write_file("task1.txt", ["hello", "hi", "goodbye"])
