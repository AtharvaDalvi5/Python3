def Check(no):
    if no > 0:
        print("Positive Number")
    elif no < 0:
        print("Negative Number")
    else:
        print("Zero")

def main():
    No = int(input("Enter number: "))
    Check(No)

if __name__ == "__main__":
    main()