import sys

def main():
    try:
        numbers = int(input("Enter a number: "))
        if numbers % 2 != 0:
            print("The number is: ", numbers)
        else:
            print("The number is even")
    except ValueError as e:
        print("Error", e, file=sys.stderr)
    finally:
        print("Thank you for using the program")

if __name__ == "__main__":
    main()

