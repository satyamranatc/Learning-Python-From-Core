a = {1,2,3,4,5,6}
b = {5,6,7,8,9,10}

a.update({1000})
a.update({1})

print(a)
print(b)

print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))


