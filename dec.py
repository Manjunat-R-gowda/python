def sure_name(arun):
    def wrapper():
        print("this is helpful")
    arun()
    return wrapper

@sure_name
def grret():
    print('enginerring in kannda python course')

@sure_name
def simple_name():
    print("This course is super complete course you watch")

grret()
