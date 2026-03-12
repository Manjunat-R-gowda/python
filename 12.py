def gen():
    yield 0
    yield 1
    yield 3
    yield 4
t=gen()
print(next(t))
print(next(t))
print(next(t))
print(next(t))

def countdown(n):
    while n>0:
        yield n
        n-=1
    
for number in countdown(5):
    print(number)




    





