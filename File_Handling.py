#Create Mode
# f1 = open('myfile.txt','x')

#Read Mode
# f1 = open('myfile.txt','r')
# print(f1.read())
# print(f1.read(10)) #The first characters will be display
# print(f1.read(10))# NExt ten characters
# print(f1.readline())
# print(f1.readlines())

#Write mode
# f1 = open('pawankalyan.txt','w')
# f1.write('He is god')
# f1.write('He is great politician')
# f1.close()
# f2 = open('pawankalyan.txt','r')
# print(f2.read())
# f2.close()

#Append Mode

# f1 = open('pawankalyan.txt','a')
# f1.write('Good husband\n')
# f1.write('Good Actor')
# f1.close()
# f2 = open('pawankalyan.txt','r')
# print(f2.read())
# f2.close()

#Python Program to copy the even and odd lines contents from a file into even.txt and odd.txt files

f1 = open('filehandling.txt','r')
f2 = open('even.txt','w')
f3 = open('odd.txt','w')

content = f1.readlines()
for i in range(len(content)):
    if i % 2 == 0:
        f2.write(content[i])
    else:
        f3.write(content[i])
f1.close()
f2.close()
f3.close()

f4 = open('even.txt','r')
f5 = open('odd.txt','r')
print(f4.read())
print(f5.read())
f4.close()
f5.close()


