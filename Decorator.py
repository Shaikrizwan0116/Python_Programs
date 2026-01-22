#Decorator : is a function that takes another function and add some functionality to it and return original function

#Beginner Style:

# def display():
#     print("This is decorator")

# def display1(fun):
#     def smartdisplay():
#         print("*****")
#         fun()
#         print("*****")
#     return smartdisplay
# a = display1(display)
# a()


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