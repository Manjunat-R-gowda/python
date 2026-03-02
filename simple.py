name=input("enter your name:-")
year=int(input("enter your year;-"))

if year >=2026:
    print("invalid age")
    sys.exit()

age=2026-year

if age <18:
    print("you are not adult")

else:
    print("you are adult")