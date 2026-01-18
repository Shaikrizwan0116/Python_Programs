num = int(input("Enter a number: "))

for row in range(num):
    for col in range(row+1):
        print("*", end=" ")
    print()

def half_pyramid(num):
    if num > 0:
        for row in range(num):
            for col in range(row+1):
                print("*", end=" ")
            print()

half_pyramid(5)
