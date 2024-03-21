# num = int(input("Enter a number: "))
# pow = int(input("Enter a power of number: "))

# square = num ** pow
# print("The power of number is",square)


def power_of_number(num,pow):
    square = num ** pow
    return square

num = int(input("Enter a number: "))
pow = int(input("Enter a power of number: "))
print("The power of number is",power_of_number(num,pow))