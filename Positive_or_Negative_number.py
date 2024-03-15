# num = int(input("Enter a number: "))
# if num > 0:
#     print(num,"is a positive number")
# else:
#     print(num,"is a negative number")

def positive_negative_number(num):
    if num > 0:
        return num,"is positive number"
    else:
        return num,"is negitive number"

num = int(input("Enter a number: "))
print(positive_negative_number(num))