# num = int(input("Enter a number: "))
# f = 0
# for i in range(1,num+1):
#     if i*(i+1) == num:
#         f=1
#         break
# if f == 1:
#     print("This is Pronic number")
# else:
#     print("This is not pronic number")

def Pronic_number(num):
    f=0
    for i in range(1,num+1):
        if i*(i+1) == num:
            print("This is Pronic number")
            break
    else:
        print("This is not pronic number")

num = int(input("Enter a number: "))
print(Pronic_number(num))