#1.How to pass a function as an argument to another function

def div(a,b):
    return a//b

def operator(func,a,b):
    print("Hello this advance function")
    result = func(a,b)
    print("This is div",result)
    print("Completed this!")

operator(div,15,5)

#2.How to return a function as a value

def operate():
    print("This advance concept")
    def execute():
        print("Like and share")
        print("Good evening")
    return execute
a = operate()
a()