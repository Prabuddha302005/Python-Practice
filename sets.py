# for i in range(1, 500, 1):
#     print("Hmmmm")

myset = {"A", "b", "c", "d"}
print(myset, type(myset))

# methods of set
# union 
a = {1, 2, 3, 4}
b = {5, 6, 7, 8}
c = a | b
print(c)

#intersection
d = {1 , 2, 3, 4, 5}
e = {1, 2, 3, 6, 8}
f = d & e
print(f)

g = {1, 2, 3, 4, 6}
h = {1, 2, 3, 4, 8, 7}
i = g - h 
print(i)
# symmentric difference
j = g ^ h
print(j)


