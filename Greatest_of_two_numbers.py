# num1 = int(input("Enter num1 number: "))
# num2 = int(input("Enter num2 number: "))

# if num1 > num2:
#     print("Greatest number is",num1)
# else:
#     print("Greatest number is",num2)

def greatest_of_two_numbers(num1,num2):
    if num1 > num2:
        return 'Greatest number is',num1
    else:
        return 'Greatest number is',num2

num1 = int(input("Enter num1 number: "))
num2 = int(input("Enter num2 number: "))

print(greatest_of_two_numbers(num1,num2))
