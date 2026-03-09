num=[2,5,7,1,4,5,6]
def is_even (num):
    return num%2==0

res=map(is_even,num)
print(list(res))


num=[4,3,5,2,4]
def add(a):
    return a*2
res=map(add,num)
print(list(res))


