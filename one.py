
day=input("enter your day:-")
is_day=True
match day:
    case "monday":
        print("duty")
    case "tuseday" if  is_day:
        print("off day duty")
    case "wednseday":
        print("full duty")
    case "thursday":
        print("leave today")
    case "friday":
        print('trip')
    case "saturday":
        print("off day")
    case "sunday":
        print("holiday")
    case _:
        print(' please try again.....!')