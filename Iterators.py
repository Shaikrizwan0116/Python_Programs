# Iterator is an object that is used to iterate over iterable objects like tuple set dict.

# n = [12,13,14]
# print(n[0])
# print(n[1])
# print(n[2])

# for i in n:
#     print(i)

#Iterator

num = [45,46,47]
it = iter(num) #Converts th list into iterator
print(it)
print(it.__next__())
print(it.__next__())
print(it.__next__())
