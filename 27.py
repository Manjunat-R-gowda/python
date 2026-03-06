def log_function_call(monk):
    def add(a,b):
        print('Result;-',end="")
        monk(a,b)
    return add
    
@log_function_call
def add(a,b):
    print(a+b)

@log_function_call
def sub(a,b):
    print(a-b)

@log_function_call
def mul(a,b):
    print(a*b)

@log_function_call
def div(a,b):
    print(a/b)

add(5,5)
sub(200,100)
mul(5,5)
div(50,2)
