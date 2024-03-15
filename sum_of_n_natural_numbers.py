# num = int(input("Enter a number: "))
# sum = 0
# while num != 0:
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10
# print("The sum of n natural numbers",sum)


def sum_of_natural_number(num):
    sum = 0
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
    return 'sum of natural numbers is',sum

num = int(input("Enter a number: "))
print(sum_of_natural_number(num))