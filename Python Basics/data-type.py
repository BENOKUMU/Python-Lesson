# Data types in python include

# Integers - they are numbers eg 10, 20
print(29)
b = 7
print(b, 'is of type', type(b))

#Complex no.
a = 1 + 2j
print(a, "is complex number", isinstance(1+2j, complex))

#Floating-point Numbers - no. with decimal points
print(4.5)
print(3.142)

#Strings - sequence of character data
print("I am Benjamin")
print('Benjamin is a software engineer')

# List - is ordered sequence of items. They are mutable
a = [1, 1.2, 'Benjamin']
print(a)

#Tuple - ordered sequence of items that are immutable
t = (5, 'progran', 1+3j)

#Set - unordered collection of unique items
a = {5, 3, 1, 5}
print(type(a))



# Variables - containers for storing data values
x = 5
name = "Benjamin"
print(x, name)

#casting
x = str(5)
z = float(5)
y = int('98')


a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
 print ("Line 1 - a is available in the given list")
else:
 print ("Line 1 - a is not available in the given list")
if ( b not in list ):
 print ("Line 2 - b is not available in the given list")
else:
 print ("Line 2 - b is available in the given list")
c=b/a
if ( c in list ):
 print ("Line 3 - a is available in the given list")
else:
    print ("Line 3 - a is not available in the given list")
