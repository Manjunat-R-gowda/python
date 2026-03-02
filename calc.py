print("1----addittion-----")
print("2----subtraction----")
print("3----multiplication---")
print('4-----division------')
print("5-----exit--------")

while True:
    a=int(input("enter your first number:-"))
    b=int(input("enter your second number:-"))
    choice=int(input("enter your choice(1-5):-"))
    if choice==1:
        print(f"This is addition {a+b}")
    elif choice==2:
        print(f"This is subtraction {a-b}")
    
    elif choice==3:
        print(f"This is multiplication {a*b}")
    elif choice==4:
        print(f"This is division {a/b}")
    elif choice==5:
        print("exit Thank you.....")
    else:
        print("choose invalid option choose correct option")
    break
print("----THANK YOU-----")