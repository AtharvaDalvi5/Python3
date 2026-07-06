def Pattern(no):
    for i in range(no):
        for j in range(no):
            print("*", end =" ")
        print()

def main():
    no = int(input("Enter number: "))
    Pattern(no)

if __name__ == "__main__":
    main()