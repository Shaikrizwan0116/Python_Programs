# num = int(input("Enter a number: "))
# if num % 7 == 0 or num % 10 == 7:
#     print(num," is buzz number")
# else:
#     print(num,"is not a buzz number")


def buzz_number(num):
    if num % 7 == 0 or num % 10 == 7:
        return num,"is buzz number"
    else:
        return num,"is not buzz number"

print(buzz_number(49))