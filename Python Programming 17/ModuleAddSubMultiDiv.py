from Arithmetic import *

def main():
    print("Enter the First Number: ")
    Value1 = int(input())

    print("Enter the Second Number: ")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)
    print("Addition is: ",Ret)

    Ret = Substraction(Value1,Value2)      
    print("Substraction is: ",Ret)

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is: ",Ret)

    Ret = Division(Value1,Value2)      
    print("Division is: ",Ret)

if __name__ == "__main__":
    main()