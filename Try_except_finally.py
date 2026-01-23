#Try, Except, Finally
# 1.Compile time errors
# 2.Run time error

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print(a//b)
except:
    print("You are enter zero")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print(a//b)
except ZeroDivisionError:
    print("You cannot divided by zero")

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter b number: "))
    print(a//b)
    list1 = [1,2,3,4]
    key1 = int(input("Enter a number: "))
    print(list1[key1]) 
except ZeroDivisionError:
    print("You cannot divided by zero")
except IndexError:
    print("There is a no value you enter")
except Exception:
    print("Something went wrong!")
finally:
    print("This is try expect block")
