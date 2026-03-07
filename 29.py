def specific_user(func):
    def view_data(name):
        if name=="admin":
            func(name)
        else:
            print("Access Denied")
    return view_data


@specific_user
def user(name):
    print("welcome you can view the data",name)

user("admin")
