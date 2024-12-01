import sys

def main():
    try:
        filename = input("Enter file name: ")
        if not filename.endswith(".txt"):
            raise NameError("File name must text file")

        with open(filename, "r") as file:
            print("Contents: ", file.read())

    except NameError as e:
        print("Name Error: ", e, file=sys.stderr)
    except FileNotFoundError as d:
        print("File Not Error: ", d, file=sys.stderr)


if __name__ == "__main__":
    main()