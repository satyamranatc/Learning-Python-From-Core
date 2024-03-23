a = [1,"Satyam",True,3.3]

# print(a)

a.append(1000)

# print(a)

x = a.pop(3)
# print("x: " , x)

a.remove("Satyam")
# print(a)

a.insert(2,"100000")
# print(a)

a= [2,4,5,6,7,2,1,3,4]

# a.sort()
# a.sort(reverse=True)
# a.reverse()

# a.clear()


# print(a.count(2))

# x = a.copy()
# x.clear()
# print(a)

# 2d List

# a = [[1,2,3],[1,2,3],[5,6,7]]

# for i in a:
#     for j in i:
#         print(j, end=" ")
#     print()

# a= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# print(a[:6:])

#Tuple:- Constant Data

t = (1,2,3,4,5,6,7,8)
print(t)
print(type(t))
print(len(t))
print(t[0])
print(t.index(2))
print(t.count(2))

#Unpacking The Tuple
t = (2,3)
a,b = t
print(a,b)