# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(num,"is even number")
# else:
#     print(num,"is odd number")

def even_or_odd(num):
    if num % 2 == 0:
        return num,"is even number"
    else:
        return num,"is odd number"

num = int(input("Enter a number: "))
print(even_or_odd(num))