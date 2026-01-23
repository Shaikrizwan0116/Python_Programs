
def spy_number(n):
    sum = 0
    prod = 1
    while n != 0:
        rem = n % 10
        sum = sum + rem
        prod = prod * rem
        n = n // 10
    return sum, prod

n = int(input("Enter a number: "))
s, p = spy_number(n)
if s == p:
    print("This is SPY number")
else:
    print("This is not a SPY number")