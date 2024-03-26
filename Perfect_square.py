# num = int(input("Enter a number: "))
# square = num * num
# sum = 0
# while square != 0:
#     rem = square % 10
#     sum = sum + rem
#     square = square // 10
# if num == sum:
#     print("Perfect number")
# else:
#     print("Not a Perfect number")


def perfect_square(num):
    sum=0
    square = num * num
    while square != 0:
        digit = square % 10
        sum = sum + digit
        square = square // 10
    if num == sum:
        return "Perfect square"
    else:
        return "Not a Perfect square"

num = int(input("Enter a number: "))
output = perfect_square(num)
print(output)