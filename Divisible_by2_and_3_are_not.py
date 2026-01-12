# num = int(input("Enter a number: "))
# if num % 2 == 0 and num % 3 == 0:
#     print(num," is divisible by 2 and 3")
# else:
#     print(num,"is not divisible by 2 and 3")

# 2nd way

num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 3 == 0:
        print(num,"is divisible by 2 and 3")
    else:
        print(num,"is not divisible by 3")
else:
    print(num,"is not divisible by 2 and 3")