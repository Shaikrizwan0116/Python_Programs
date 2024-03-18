# num = int(input("Enter a number: "))
# rev = 0
# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# print("The Reverse of number is",rev)

def reverse_number(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return "The Reverse number is",rev

    
num = int(input("Enter a number:"))
print(reverse_number(num))