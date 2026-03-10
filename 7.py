from functools import reduce
num=[4,5,6,8,3,2,4,5,6,6]
def add (x,y):
    return x+y
res=reduce(add,num)
print(res)


from functools import reduce
num=[5,4,7,6,5,8]
def mul(x,y):
    return x*y
res=reduce(mul,num)
print(res)

from functools import reduce
num=[5,6,7,8,34,5,67,6,5,4,5,6,66]
def large_num():
    return 
res=reduce(max,num)
print(res)


from functools import reduce
num=[5,6,7,8,34,5,67,6,5,4,5,6,66]
def large_num():
    return 
res=reduce(min,num)
print(res)