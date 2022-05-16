####SOLUTIONS
#1
for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz") 
    else:
        print(x)

#2
a = "Fizz"
b = "Buzz"
for x in range(1, 101):
    print(a+b if x%15 == 0 else a if x%3==0 else b if x%5 == 0 else x)

#3
for x in range(1, 101):
    print("FizzBuzz" if x%3==0 and x%5==0 else "Fizz" if x%3==0 else "Buzz" if x%5==0 else x) 

#4
for x in range(1,101):
 if x%15==0:print("FizzBuzz")
 elif x%3==0:print("Fizz")
 elif x%5==0:print("Buzz")
 else:print(x)