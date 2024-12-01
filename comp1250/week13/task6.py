import sys

def main():
    try:
        numbers = (int(input("Enter a number: ")))
        print("Number is: ", numbers)
    except ValueError as e:
        print("Error", e, file=sys.stderr)
    finally:
        print("Thank you for using the program")

if __name__ == "__main__":
    main()