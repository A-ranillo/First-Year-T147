import os

def main():
    filenames = os.listdir()
    for filename in filenames:
        print("Files/Directory",filename)

if __name__ == '__main__':
    main()

