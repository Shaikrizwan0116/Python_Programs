#Program to pass an entire list of element (even or odd) number count

def even_odd(list1):
    even = 0
    odd = 0
    for i in list1:
        if i % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    return even, odd
list1 = [1,2,3,4,5,6,7,8,9,10]
e, o = even_odd(list1)
print("The Even numbers",e)
print("The odd numbers",o)