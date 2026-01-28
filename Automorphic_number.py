# num = int(input("Enter a number: "))
# square = num * num
# while square != 0:
#     rem = square % 10
#     if rem == num:
#         print("This is automorphic number")
#         break
# else:
#     print("This is not automorphic number")


def automorphic_number(num):
    square = num * num
    if square % 10 == num:
        print("This is automorphic number")
    else:
        print("This is not a automorphic number")

print(automorphic_number(5)) 