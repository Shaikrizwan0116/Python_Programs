num = int(input("Enter a number of elements: "))
num1 = int(input("Enter a First element: "))
num2 = int(input("Enter a Second element: "))

if num < 0:
    print("Please enter a positive number")
elif num == 0:
    print("The fabinacci number",1)
else:

    for i in range(1,num-1):
        num3 = num1 + num2
        print(num3)
        num1 = num2
        num2 = num3