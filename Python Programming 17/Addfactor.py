def AddFactors(no):
    sum = 0
    for i in range(1, no):
        if no % i == 0:
            sum = sum + i
    return sum

def main():
    print("enter the number ")
    no = int(input())

    print("Factorial =", AddFactors(no))

if __name__ == "__main__":
    main()