start = int(input("Enter Start number: "))
stop = int(input("Enter Stop number: "))

for i in range(start, stop+1):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print("This is are Prime numbers",i)

def prime_numbers(start, stop):
    d = 0
    for i in range(start, stop+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print("This ar prime numbers",i)
prime_numbers(1,10)