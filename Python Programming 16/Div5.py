def CheckDiv(no):
    if no % 5 == 0:
        return True
    else:
        return False

def main():
    no = int(input("Enter number: "))
    ans = CheckDiv(no)
    print(ans)

if __name__ == "__main__":
    main()