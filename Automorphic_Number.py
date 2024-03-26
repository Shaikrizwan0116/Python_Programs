def automorphic_number(num):
    square = num * num
    if square % 10 == num:
        return "Automorphic number"
    else:
        return "Not an Automorphic number"

num = int(input("Enter a number: "))
output = automorphic_number(num)
print(output)