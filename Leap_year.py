# year = int(input("Enter year: "))

# if year % 4 == 0 and year % 100 != 0:
#     print("Leap year",year)
# elif year % 400 == 0 and year % 100 == 0:
#     print("Leap year",year)
# else:
#     print("Not a leap year")

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
        return True
    return False

year = int(input("Enter a year: "))
if leap_year(year):
    print("This is leap year")
else:
    print("This is not a leap year")