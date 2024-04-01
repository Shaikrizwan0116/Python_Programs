num1 = int(input("Enter a First number: "))
num2 = int(input("Enter a second number: "))
lcm = 1
if num1 > num2:
    maximum = num1
else:
    maximum = num2

for i in range(maximum,1+(num1*num2)):
    if (i % num1 == 0 and i % num2 == 0):
        lcm = i
print(lcm)
