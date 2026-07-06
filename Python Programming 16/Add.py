def Add(no1, no2):
    return no1 + no2

def main():
    No1 = int(input("Enter first number: "))
    No2 = int(input("Enter second number: "))
    ans = Add(No1, No2)

    print("Addition is:", ans)

if __name__ == "__main__":
    main()