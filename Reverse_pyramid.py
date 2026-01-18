for row in range(5,0,-1):
    for col in range(row):
        print("*", end=" ")
    print()

num = int(input("Enter a number of stars: "))
if num > 0:
    for row in range(num,0,-1):
        for col in range(row):
            print("*", end=" ")
        print()

