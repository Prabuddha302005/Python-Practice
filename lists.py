myList = [1, 2, "Lucky", True]
print(myList)

# list methods
myList.append(5)
print(myList)

myList.pop()
print(myList)

myList.insert(5, 0)
print(myList)

myList.extend([False, "Iron-man", 451])
print(myList)

print(myList[0])

del(myList[2])
print(myList)

myList[2] = "Lucky"
print(myList)

#List slicing
print(myList[1:4])
print(myList[3:])
print(myList[-3:])


print(len(myList))
# print(max(myList))

print(myList.count(2))

print(myList.index(False))
myList.reverse()
print(myList)






