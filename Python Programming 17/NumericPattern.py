def Pattern(no):
    for i in range(no):
        for j in range(1, no + 1):
            print(j, end="")
        print()

def main():
    num = int(input("Enter number: "))
    Pattern(num)

if __name__ == "__main__":
    main()