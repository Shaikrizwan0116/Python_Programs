num = int(input("Enter a number: "))
sum = 0
temp = num
while num != 0:
    rem = num % 10
    fact = 1
    for i in range(1,rem+1):
        fact = fact * i
    sum = sum + fact
    num = num // 10
print(sum)
if sum == temp:
    print("Strong number")
else:
    print("Not a strong number")