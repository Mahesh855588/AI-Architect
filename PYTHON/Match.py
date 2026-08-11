# This is similar to switch case
day=int(input())
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("wednesday")
    case 4:
        print("thursday")
    case 5:
        print("friday")
    case 6:
        print("saturday")
    case 7:
        print("sunday")
    case _:
        print("enter correct input")


# multiple values in one case
day=int(input())
match day:
    case 1|2|3|4|5:
        print("weekday")
    case 6|7:
        print("weekend")
    case _:
        print("enter correct value")