def list_items(list1):
    sum = 0
    for i in list1:
        sum += i
    return sum
list1 = [1,2,3,4]
a = list_items(list1)
print("The list items", a)