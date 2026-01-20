a = {1:"Python", 2:"Django", 3:"JavaScript"}
# print(a)
# print(type(a))
a[4]="MYSQL"
# print(a)

a[4] = "HTMl"
# print(a)

a.pop(4)
# print(a)

a.popitem()
# print(a)

b = {1:"Rizwan"}
c = {2:"Rizu"}
# print(a+b) unsupported

b = c.copy()
# print(b)

z = {1:"Rizwan", 2:"Rizu"}
z.clear()
print(z)