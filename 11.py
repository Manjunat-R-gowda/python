#practise iterators and generrators
l=[2,3,4,5,6,7]
print(type(l))
print(l)

it=(i*i for i in range(3))
print(next(it))
print(next(it))
print(next(it))
print(type(it))

for i in range(1,11):
    print(i)
