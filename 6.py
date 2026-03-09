num=[2,5,7,1,4,5,6]
def is_even (num):
    return num%2==0

res=filter(is_even,num)
print(list(res))

num=[2,5,7,1,4,5,6]
def is_odd (x):
    return x%2!=0

res=filter(is_odd,num)
print(list(res))


numbers=[3,4,6,5,2,34,5,3,2,3,4,4,4,]
res=filter(lambda x:x>5,numbers)
print(list(res))