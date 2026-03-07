def profile_name(func):
    def adds(name):
        print("==")
        func(name)
    return adds

def belpw_profile(fun):
    def below(name):
        print(">>>>>>",end=" ")
        fun(name)
    return below


@profile_name
@belpw_profile
def greet(name):
    print(f"{name}")

greet("manjunath")
