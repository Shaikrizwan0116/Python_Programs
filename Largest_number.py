a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
if a > b:
    print(a,"is largest number")
else:
    print(b,"is largest number")

def largest_number(a, b):
    if a > b:
        return a,"is a largest number"
    else:
        return b,"is a largest number"

print(largest_number(12,14))