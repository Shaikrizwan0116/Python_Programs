#Lambda function Application
# 1.filter
# 2.map
# 3.reduce

#1.filter

# def iseven(n):
#     return n % 2 == 0
# num = [1,2,3,4,5,6,7,8,9,10]

# nums = list(filter(iseven,num))
# print(nums)

# num = [1,2,3,4,5,6,7,8,9,10]
# evens = list(filter(lambda n:n%2==0, num))
# print(evens)


##Map Function
# def mul(n):
#     return n * 2

# num = [1,2,3,4,5,6,7,8,9,10]

# map1 = list(map(mul,num))
# print(map1)

# map1=list(map(lambda n:n*2, num))
# print(map1)


##Reduce
from functools import reduce
num = [1,2,3,4,5,6,7,8,9,10]
reduce1 = reduce(lambda a,b:a+b, num)
print(reduce1)




