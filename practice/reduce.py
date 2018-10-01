from functools import reduce

mylist = ['hello', 'world']
#unique = reduce(lambda l, x: l.append(x) or l if x not in l else l, mylist, [])
unique=reduce(lambda x,y: x.union(y), mylist, set())


print(unique)