list1 = [12,13,14,15]
key = int(input("Enter the element to be searched: "))
for i in list1:
    if i == key:
        print(key, "is found")
        break
else:
    print(key,"is not found")

for i in range(1,11):
    if i == 5:
        break
    else:
        print(i)

for i in range(0,10,2):
    print(i)

for i in range(0,10,2):
    if i == 6:
        break
    else:
        print(i)


# Continue

for i in range(0,10):
    if i == 5:
        continue
    else:
        print(i)

for i in range(1,11):
    if i == 4 or i == 6:
        continue
    else:
        print(i)

for i in range(1,11):
    if i == 4 or i == 5:
        continue
        print("safa")
    else:
        print(i)

# Pass

a = 5
b = 5

if a != b:
    pass
else:
    print("Hello")

for i in range(1,11):
    pass
print("I  dont want to print anything")

