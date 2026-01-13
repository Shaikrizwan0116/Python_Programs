a = int(input("Enter A value: "))
b = int(input("Enter B Value: "))
ch = int(input("Please enter option number: "))

if ch == 1:
    print("Addition is", a+b)
elif ch == 2:
    print("Sub is", a-b)
elif ch == 3:
    print("mul is", a*b)
elif ch == 4:
    print("Division is", a/b)
elif ch == 5:
    print("Floor division is", a//b)
elif ch == 6:
    print("Module is", a%b)
else:
    print("Invalid")