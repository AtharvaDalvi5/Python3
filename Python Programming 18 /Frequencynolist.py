def Frequency(Data, Value):
    Count = 0

    for no in Data:
        if no == Value:
            Count = Count + 1

    return Count

def main():
    Size = 0
    Arr = list()

    print("Enter the number of elements:")
    Size = int(input())

    print("Enter the elements:")
    for i in range(Size):
        no = int(input())
        Arr.append(no)

    print("Enter element to search:")
    Search = int(input())

    Ret = Frequency(Arr, Search)

    print("Frequency is :", Ret)

if __name__ == "__main__":
    main()
