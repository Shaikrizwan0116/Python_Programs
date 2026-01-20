# def list_items(list1):
#     sum = 0
#     for i in list1:
#         sum += i
#     return sum
# list1 = [1,2,3,4]
# a = list_items(list1)
# print("The list items", a)

def even_odd(list1):
    even = 0
    odd = 0
    for i in list1:
        if i % 2 == 0:
            even += i
        else:
            odd += i
    return even, odd
list1 = [1,2,3,4,5,6,7,8,9,10]
e,o = even_odd(list1)
print("The Even numbers count",e)
print("The odd number count",o)