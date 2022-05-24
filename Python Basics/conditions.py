var1 = 100
if var1:
    print("1 - Got a true expression value")
    print(var1)
    
    
var2 = 0
if var2:
    print("2 - Got a true expression value")
    print(var2)
    
print("Good bye!")



amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)
    
print ("Net payable:", amount - discount)




amount = int(input("Enter amount: "))
if amount < 1000:
    discount = amount * 0.05
    print("Discount", discount)
elif amount < 5000:
    discount = amount * 0.10
    print("Discount", discount)
else:
    discount = amount * 0.10
    print("Discount", discount)
    
print ("Net payable:", amount - discount)



if mu%2==0:
    if num%3==0:
        print("Divisible by 3 and 2")
    else:
        print("divisible by 2 not divisible by 3")
else:
    if num%3==0:
        print("divisible by 3 not divisible by 2")
    else:
        print("divisible by 2 and not 3")


var = 100
if (var == 100): print("value of expression is 100")
print("Good Bye!")