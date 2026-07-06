def Length(name):
    return len(name)

def main():
    name = input("Enter name: ")
    ans = Length(name)
    print("Length is:", ans)

if __name__ == "__main__":
    main()