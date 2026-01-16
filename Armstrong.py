num = int(input("Enter a number: "))
d = 0
temp = num

while num != 0:
    d = d+1
    num = num // 10
print("The no of digits:",d)
num = temp
sum = 0
while num != 0:
    rem = num % 10
    sum = sum + rem ** d
    num = num // 10
if sum == temp:
    print(temp," is armstrong number")
else:
    print(temp,"is not armstrong number")