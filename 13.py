num=(x*x for x in range(1,10))

print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


import sys
l=[x for x in range(1,1000000)]
sys.getsizeof(l)
print(type(l))


g=(x for x in range(1,100000))
sys.getsizeof(g)
print(type(g))