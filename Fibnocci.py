num = int(input("Enter a number pf elements: "))
num1 = int(input("Enter a first element: "))
num2 = int(input("Enter a second element: "))

if num < 0:
    print("Enter a positive number")
elif num == 0:
    print("The value of fibnocci series is",num1)
else:
    for i in range(1,num-1):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3
