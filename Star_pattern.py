for row in range(0,4):
    for col in range(0,4):
        print("*", end=" ")
    print()

num = int(input("Enter a number: "))
if num > 0:
    for row in range(num):
        for col in range(num):
            print("*", end=" ")
        print()