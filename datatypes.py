print("Learning datatypes")

# text type ---> str
myString = "I am Python and Powerful"
print(myString)
print(type(myString))

# Numeric Types ---> int, float, complex 
myInt = 12
myFloat = 12.2
myComplex = 1j
print(type(myInt))
print(type(myFloat))
print(type(myComplex))

# Sequence Types ---> list, tuple, range
myList = ["Porsche", "Audi", "BMW", "Mercedes"]
print(myList)
print(type(myList))

myTuple = ("Samsung", "Apple", "Microsoft", "Google")
print(myTuple) 
print(type(myTuple))

myRange = range(6)
print(myRange)
print(type(myRange))

# Mapping Type --->	dict

myDict = {"name": "Steve", "Surname": "Jobs", "Position": "CEO"}

print(myDict)
print(type(myDict))

# Set Types ---> set, frozenset
mySet = {"Amazon", "Netflix", "Disney"}
print(mySet)
print(type(mySet))

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

# Boolean Type --->	bool
myBool = True
print(myBool)
print(type(myBool))

# Binary Types--->bytes, bytearray, memoryview
x1 = b"Hello"
print(x1)
print(type(x1))

x2 = bytearray(5)
print(x2)
print(type(x2))

x3 = memoryview(bytes(5))
print(x3)
print(type(x3))

# None Type ---> none
none = None
print(None)
print(type(None))