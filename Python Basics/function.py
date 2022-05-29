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