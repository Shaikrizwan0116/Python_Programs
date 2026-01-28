#Generator: Generator is a function like a normal function but when ever it needs to generator a value it does so with the yield statement instead of return statement

#Yield: The yield statement suspends a function execution and sedns a value back to the caller but retains enough state to execute the function to resume when it left off


#General Function
# def fun():
#     return 1
#     return 2
#     return 3
# a = fun()
# print(a)

#Generator

def fun():
    yield 1
    yield 2
    yield 3
for i in fun():
    print(i)
