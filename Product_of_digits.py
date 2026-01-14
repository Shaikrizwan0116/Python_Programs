# num = int(input("Enter a number: "))
# prod = 1
# while num != 0:
#     rem = num % 10
#     prod = prod * rem
#     num = num // 10
# print("The product of number", prod)

def product_of_digits(num, prod=1):
    while num != 0:
        rem = num % 10
        prod = rem * prod
        num = num // 10
    return "The Product of digits",prod

print(product_of_digits(1234))