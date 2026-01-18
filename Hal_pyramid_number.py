# num = int(input("Enter a number: "))
# if num > 0:
#     for row in range(num):
#         for col in range(row+1):
#             print(col+1,end=" ")
#         print()


num = int(input("Enter a number: "))
if num > 0:
    for row in range(num,0,-1):
        for col in range(row):
            print(col+1,end=" ")
        print()