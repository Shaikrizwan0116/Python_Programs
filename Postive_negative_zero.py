# num = int(input("Enter a number: "))
# if num > 0:
#     print(num,"is positive number")
# elif num ==0:
#     print(num,"is zero")
# else:
#     print(num,"is negative number")

def Positive_negative_zero(num):
    if num > 0:
        return num,"is positive number"
    elif num == 0:
        return num,"is zero"
    else:
        return num,"is negative number"

print(Positive_negative_zero(12))