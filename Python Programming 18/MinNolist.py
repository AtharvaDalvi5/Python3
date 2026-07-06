def Min(Data):
    Min = Data[0]

    for no in Data:
        if no < Min:
            Min = no

    return Min

def main():
    Size = 0
    Arr = list()

    print("Enter the number of elements:")
    Size = int(input())

    print("Enter the elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    Ret = Min(Arr)

    print("Maximum number is :", Ret)

if __name__ == "__main__":
    main()