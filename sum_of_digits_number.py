# num = int(input("Enter a number: "))
# sum = 0
# while num != 0:
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10
# print("The sum of digits is",sum)

def sum_of_digits_number(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return "The sum of digits of numbers is",sum

num = int(input("Enter a number: "))
print(sum_of_digits_number(num))