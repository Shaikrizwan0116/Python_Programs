# num = int(input("Enter a number: "))
# sum = 0
# while num != 0:
#     rem = num % 10
#     sum = sum + rem
#     num = num // 10
# print("The sum of digits", sum)

def sum_of_digit(num,sum=0):
    while num != 0:
        rem = num % 10
        sum = sum + rem
        num = num // 10
        return "The sum of digits",sum
        
print(sum_of_digit(1234))