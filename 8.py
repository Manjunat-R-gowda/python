from functools import reduce

score=[15,67,65,43,55,65,54,34,45,65]

updated=list(map(lambda x:x+5,score))

passing=(list)(filter(lambda x:x>=35,updated))

stu=reduce(lambda x,y:x+y,passing)


print("score:-",score)
print("updated:-",updated)
print("passing students:-",passing)
print("total student marks:-",stu)