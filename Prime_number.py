num = int(input("Enter a number: "))
if num > 0:
    for i in range(2,num):
        if num % i == 0:
            print("This is not prime number")
            break
    else:
        print("This is prime number")



def prime_number(num):
    if num > 0:
        for i in range(2,num):
            if num % i == 0:
                return num,"This is not prime number"
                break
        else:
            return num,"This is Prime number"

print(prime_number(4))
