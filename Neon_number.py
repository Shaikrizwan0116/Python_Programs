# num = int(input("Enter a number: "))
# square = num * num
# sum = 0
# while square != 0:
#     rem = square % 10
#     sum = sum + rem
#     square = square // 10

# if sum == num:
#     print("It's a neon number")
# else:
#     print("It's not a neon number")

def neon_number(num):
    square = num * num
    sum = 0
    while square != 0:
        rem = square % 10
        sum = sum + rem
        square = square // 10
    if sum == square:
        return "It's a neon number"
    else:
        return "It's not a neon number"

num = int(input("Enter a number: "))
output = neon_number(num)
print(output)