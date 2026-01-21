# set is collection of unique element but it is unordered, unindexed


s = {0,1,2,3,4,"Rizwan",True}
print(s)

print(type(s))


s.add(10)
print(s)
s.add(20)
print(s)

s.update([12,13])
print(s)

a = {1,2,3}
b = {4,5,6}
print(a | b)
print(a&b)
print(a-b)
print(b-a)
a.remove(1)
print(a)