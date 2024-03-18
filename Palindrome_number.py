# num = int(input("Enter a number: "))
# rev = 0
# temp = num

# while num != 0:
#     rem = num % 10
#     rev = rev * 10 + rem
#     num = num // 10
# if temp == rev:
#     print("Palindrome number")
# else:
#     print("Not a Palindrome number")

def palindrome_number(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev

num = int(input("Enter a number: "))

if palindrome_number(num):
    print("Palindrome number")
else:
    print("Not a palindrome number")