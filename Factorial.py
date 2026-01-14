num = int(input("Enter a number: "))
fact = 1
if num < 0:
    print("The factorial number is invalid",num)
elif num == 0:
    print("The factorial number is",fact)
else:
    for i in range(1,num+1):
        fact = fact * i
    print("The factorial",num,"is", fact)

def factorial(num, fact=1):
    if num < 0:
        print("The factorial number is invalid")
    elif num == 0:
        print("The factorial number is", fact)
    else:
        for i in range(1,num+1):
            fact = fact * i
        print("The factorial number is",fact)

print(factorial(5))