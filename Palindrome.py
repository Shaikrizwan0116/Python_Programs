num = int(input("Enter a number: "))
rev = 0
temp = num
while num != 0:
    rem = num % 10
    rev = rev * 10 + rem
    num = num // 10
if rev == temp:
    print(temp,"is a palindrome number")
else:
    print(temp,"is not palindrome number")

def palindrome(num, rev=0):
    temp = num
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    if temp == rev:
        return temp,'is palindrome number'
    else:
        return temp,'is not palindrome number'

print(palindrome(152))