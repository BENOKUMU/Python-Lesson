# import math
# import random

# print(math.pi)
# random.random()

#Numbers
# width = 20
# height = 5 * 9
# print(width * height)

# #Strings
# print('doesn\'t')

# a, b = 0, 1
# while a < 10:
#     print(a)
#     a, b = b, a + b


# a, b = 0, 1
# while a < 100:
#     print(a, end =',')
#     a, b = b, a+b


#control flow

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('negative changed to zero')
elif x == 0:
    print(0)
elif x == 1:
    print('Single')
else:
    print('More')