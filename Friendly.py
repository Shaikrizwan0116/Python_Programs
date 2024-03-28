# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# sum1 = 0
# sum2 = 0

# for i in range(1,num1):
#     if num1 % i == 0:
#         sum1 += i

# for j in range(1,num2):
#     if num2 % j == 0:
#         sum2 += j

# if (sum1 % num1 == 0 and sum2 % num2 == 0):
#     print("Yes they are a friendly pair")
# else:
#     print("No, they are not friendly")


def friendly(num1, num2):
    sum1 = 0
    sum2 = 0
    for i in range(1,num1):
        if num1 % i == 0:
            sum1 += i
    for j in range(1,num2):
        sum2 += j

    if (sum1 % num1 == 0 and sum2 % num2 == 0):
        return "Yes They are friendly numbers"
    else:
        return "No, They are not friendly numbers"

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number"))

output = friendly(num1,num2)
print(output)