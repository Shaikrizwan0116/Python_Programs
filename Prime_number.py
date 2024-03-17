num = int(input("Enter a number: "))
f = 0

if num > 0:
    for i in range(2,num):
        if num % i == 0:
            f = 1
            break
if f == 1:
    print("Not a Prime number")
else:
    print("Prime number")
