num = int(input("Enter a number: "))
sum = 0
for i in range(1,num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print("This is perfect number",num)
else:
    print("This is not a perfect number",num)