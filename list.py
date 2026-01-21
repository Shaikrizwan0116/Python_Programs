list1 = [1,2,3,4,5,"Python",True,4+6j]
print(type(list1))

# adding element

list1.append(6)
print(list1)

#Inserting element in particular place
list1.insert(0,10)
print(list1)

#Inserting multiple element in last

list1.extend([130,140])
print(list1)

#remove last element

list1.pop()
print(list1)

list1.pop(0)
print(list1)

list1.pop(5)
print(list1)

#Concatention

list1 = [1,2,3]
list2 = ['python', 'Java']
print(list1+list2)

print(list1*2)

# slicing

list1 = [0,1,2,3,4,5,6,7,8,9,10]
print(list1[0:5])
print(list1[1:5])
print(list1[:4])
print(list1[:3])
print(list1[-1])
print(list1[::-1])


list1 = [1,2,3,4,5,6]
for i in list1:
    print(i)
for i in list1[0:5]:
    print(i)