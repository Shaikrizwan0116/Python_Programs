# num = int(input("Enter a number"))
# fact = 1
# sum = 0
# for i in range(1,num):
#     if num % i == 0:
#         sum = sum + i
# if num < sum:
#     print("It's an abundant number")
# else:
#     print("It's not an abundant number")

def abundant_number(num):
    fact = 1
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if num < sum:
        return("It's an abundant number")
    else:
        return "It's not an abundant number"

num = int(input("Enter a number: "))
output = abundant_number(num)
print(output)