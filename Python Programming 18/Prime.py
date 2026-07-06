import MarvellousNum

def ListP(Data):
    Sum = 0

    for no in Data:
        if MarvellousNum.Prime(no):
            Sum = Sum + no

    return Sum

def main():
    Size = 0
    Arr = list()

    print("Enter the number of elements:")
    Size = int(input())

    print("Enter the elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    Ret = ListP(Arr)

    print("Addition of prime numbers is :", Ret)

if __name__ == "__main__":
    main()