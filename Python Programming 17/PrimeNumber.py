def Prime(no):
    count = 0

    for i in range(1, no + 1):
        if no % i == 0:
            count = count + 1

    if count == 2:
        print("It is Prime Number")
    else:
        print("It is Not Prime Number")

def main():
    num = int(input("Enter number: "))
    Prime(num)

if __name__ == "__main__":
    main()