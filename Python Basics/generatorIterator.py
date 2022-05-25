import sys
# list = [1,2,3,4,5]
# it = iter(list) #builds an iterator object
# print(next(it)) #prints next available in iterator

# for x in it:
#     print(x, end = ' ')
    
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
        

def fibonacci(n): #generator function
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(5) #f is iterator object
while True:
    try:
        print (next(f), end=" ")
    except StopIteration:
        sys.exit()
