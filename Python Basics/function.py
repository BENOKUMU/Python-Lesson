# def functionname( parameters ):
#     "function_doctstring"
#     function_suite
#     return [expression]

def printme(str):
    "This prints a passed string into this function"
    print(str)
    return

printme("My nickname is Benwaves and I like it very much")

def changeme(myList):
    print("Values inside the function before change: ", myList)
    myList[2] = 50
    print("Values inside the function after the change: ",myList)
    return

myList = [10,20,30,40]
changeme(myList)
print(myList)

#keyword argument
def printme(str):
    print (str)
    return
printme(str = "my String")

def printinfo(name, age):
    print("Name: ", name)
    print("Age: ", age)
    return
printinfo(name="miki", age=23)

total = 0 # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
    # Add both the parameters and return them."
    total = arg1 + arg2; # Here total is local variable.
    print ("Inside the function local total : ", total)
    return total
# Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )

