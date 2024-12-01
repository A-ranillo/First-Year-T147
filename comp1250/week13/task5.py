import os

def main():
    os.makedirs('d1/d2/d3', exist_ok=True)
    open("d1/file1.txt", "a")
    open("d1/file2.txt", "a")

    open("d1/d2/file1.txt", "a")
    open("d1/d2/file2.txt", "a")

    open("d1/d2/d3/file1.txt", "a")
    open("d1/d2/d3/file2.txt", "a")

if __name__ == "__main__":
    main()

