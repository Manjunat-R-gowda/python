#practisce iterators and generators
ram=["kgf","kantara","rajakumara","ranna","abhi"]

num=iter(ram)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))


class even_numbers:
    def __init__(self,limit):
        self.limit=limit
        self.current=0

    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.limit:
            res=self.current
            self.current+=2
            return res
        
        else:
             raise StopIteration
        
s=even_numbers(34)
for i in s:
    print(i)
