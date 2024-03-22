num = int(input("Enter a number: "))
sum = 0
fact = 1
for i in range(1,num):
    if num % i == 0:
        sum = sum + i
if num == sum:
    print("It's a perfect number")
else:
    print("It's not a perfect number")
