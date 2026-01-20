num = int(input("Enter a number: "))
square = num * num
sum = 0
while square != 0:
    rem = square % 10
    sum = sum + rem
    square = square // 10
if sum == num:
    print("The Neon number")
else:
    print("This is not a neon number")
