# start = int(input("Enter start number: "))
# stop = int(input("Enter stop number: "))
# sum = 0

# for i in range(start,stop+1):
#     sum = sum + i
# print("The sum of number is",sum)

def sum_of_number_given_range(start,stop):
    sum = 0
    for i in range(start,stop+1):
        sum = sum + i
    return 'The sum of numbers is',sum

start = int(input("Enter start number: "))
stop = int(input("Enter stop number: "))

print(sum_of_number_given_range(start,stop))