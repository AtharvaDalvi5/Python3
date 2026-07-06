def Sum(no):
    sum = 0

    while no > 0:
        digit = no % 10
        sum = sum + digit
        no = no // 10

    return sum

def main():
    n = int(input("Enter number: "))
    print("Addition of digits =", Sum(n))

if __name__ == "__main__":
    main()