def Pattern(no):
    for i in range(no, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()

def main():
    no = int(input("Enter number: "))
    Pattern(no)

if __name__ == "__main__":
    main()