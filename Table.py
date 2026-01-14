num = int(input("Enter a Table: "))
s = int(input("Enter a number: "))
for i in range(1,s+1):
    print(num,"*",i,"=",num*i)

def table(num,s):
    for i in range(1,s+1):
        print(num,"*",i,"=",num*i)
        
print(table(5,10))