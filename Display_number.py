# Display 1 to 10 number using forloop
num = int(input("Enter a number: "))
for i in range(0,num+1):
    print(i)

# Using function display number
def display_number(num):
    for i in range(0,num+1):
        print(i)

print(display_number(10))

# Printing even numbers
num = int(input("Enter a number: "))
for i in range(0,num+1):
    if i % 2 == 0:
        print("Even number: ",i)
        
#Printing even and odd numbers using forloop
num = int(input("Enter a number: "))
for i in range(0,num+1):
    if i % 2 == 0:
        print("Even number",i)
    else:
        print("Odd number",i)
