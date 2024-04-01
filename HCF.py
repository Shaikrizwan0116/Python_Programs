# #highest common factor

# num1 = int(input("Enter a number1: "))
# num2 = int(input("Enter a number2: "))
# hcf = 1
# for i in range(1,min(num1,num2)):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
# print("The highest common factor is ",hcf)

def hcf_number(num1, num2):
    if num1 > num2:
        smallest = num2
    else:
        smallest = num1
    
    hcf = 1
    for i in range(1,smallest+1):
        if (num1 % i == 0 and num2 % i == 0):
            hcf = i
    return hcf

num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number"))
output = hcf_number(num1, num2)
print(output)