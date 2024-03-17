# num1 = int(input("Enter First number: "))
# num2 = int(input("Enter Second number: "))
# num3 = int(input("Enter Third number: "))

# if num1 > num2 and num1 > num3:
#     print("The greatest number is",num1)
# elif num2 > num1 and num2 > num3:
#     print("The greatest number is",num2)
# else:
#     print("The greatest number is",num3)

def greatest_three_number(num1,num2,num3):
    if num1 > num2 and num1 > num3:
        return "The greatest number is",num1
    elif num2 > num3 and num2 > num3:
        return "The greatest number is",num2
    else:
        return "The greatest number is",num3

num1 = int(input("Enter First number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

print(greatest_three_number(num1,num2,num3))