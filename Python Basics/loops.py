
count = 0
while (count < 9):
    print("The count is:", count)
    count = count + 1
print("Good bye!")


var = 1
while var == 1:
    num = int(input("Enter a number: "))
    print("You entered: ")
print("Good bye!")


for letter in 'Benjamin':
    print("current letter:", letter)
print()
fruits = ['banana', 'apple', 'mango']
for fruits in fruits:
    print('current fruit:, fruit')
print('Good bye!')

numbers = [11,33,55,39,55,74,23,21,41,13]
for num in numbers:
    if num%2 == 0:
        print('The list contain an even number')
        break
else:
    print('The list doesnt contain even number')

for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print(k, end= ' ')
    print()

no = int(input('any number: '))
numbers = [11,33,55,39,55,74,23,21,41,13]
for num in numbers:
    if num == no:
        print('number found in list')
        break
    else:
        print('number not found in list')
        break

