# num = int(input("Enter a number: "))
# temp = num
# sum = 0
# while num != 0:
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10
# if temp % sum == 0:
#     print("Harshad number")
# else:
#     print("Not a harshad number")

def harshad_number(num):
    temp = num
    sum = 0
    while num != 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    if temp % sum == 0:
        return "It's harshad number"
    else:
        return "Not a harshad number"

num = int(input("Enter a number: "))
output = harshad_number(num)
print(output)