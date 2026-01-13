# year = int(input("Enter a year: "))
# if year % 4 == 0 and year % 100 != 0:
#     print(year,"is a leap year")
# elif year % 100 == 0 and year % 400 == 0:
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")

def leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return year,"is a leap year"
    elif year % 100 == 0 and year % 400 == 0:
        return year,"is a leap year"
    else:
        return year,"is not a leap year"

print(leap_year(2024))