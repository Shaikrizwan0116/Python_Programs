#Global and local variable

# a = 10 #Global variable
# def display():
#     print("a value inside a function is",a) #a=10
# display()
# print("a value outside of function",a) #a=10

# a = 10
# def display():
#     a = 20
#     print("a value inside the function",a) #a=20
# display()
# print("a value outside the function",a) #a=10

# a=10
# def display():
#     global a
#     a=20
#     print("a value inside the function",a) #a=20
# display()
# print("a value outside the function",a) #a=20

a=10
def display():
    a = 20
    print("a value inside the function",a)
    x = globals()['a']
    globals()['a']=100
display()
print("a value outside the function",a)