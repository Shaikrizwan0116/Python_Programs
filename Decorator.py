#Decorator : is a function that takes another function and add some functionality to it and return original function

#Beginner Style:

def display():
    print("This is decorator")

def display1(fun):
    def smartdisplay():
        print("*****")
        fun()
        print("*****")
    return smartdisplay
a = display1(display)
a()


def display1(fun):
    def smartdisplay():
        print("*****")
        fun()
        print("*****")
    return smartdisplay

@display1
def display():
    print("The is showing something")
display()

## Decorators with parameters

def smart_div(fun):
    def inner_func(a,b):
        print("Welcome to PT")
        if b == 0:
            print("Cant divided")
            return
        return fun(a,b)
    return inner_func

@smart_div
def div(a,b):
    return a//b
result_div = div(15,3)
print(result_div)