print("Operators in Python")

# Arthimetic operators + - / * %

print("Arthimetic operators")
x = 10
y = 12
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

# Python Comparison Operators
# Comparison operators are used to compare two values:

print("Comparison operators")
a = 12
b = 13
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a >= b)
print(a <= b)

# Python Logical Operators
# Logical operators are used to combine conditional statements:

print("Logical operators")

xx = 25
print(xx < 26 and xx <= 25)
# and operator only works when both the conditions are true

print(xx < 28 or xx < 22)
# or returns true if one of the statements is true 

print(not(xx <= 23 and xx <= 24))
# not Reverse the result, returns False if the result is true


# Python Identity Operators
print("Python Identity Operators")
# is 
xObj = ["apple", "banana"]
yObj = ["apple", "banana"]
zObj = xObj
# Returns True if both variables are the same object
print(xObj is zObj)
print(xObj is yObj)
print(xObj == yObj)
# is not	
# Returns True if both variables are not the same object

# Python Membership Operators
print("Python Membership Operators")
name = "Lucky"
if ("L" in name):
    print("Yes!")
else:
    print("No!")

carName = "Porsche"
if ("J" not in carName):
    print("Yes! Not Exists")
else:
    print("No! I exists")