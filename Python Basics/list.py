
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

list1[0]
list[1:5]

print("Value available at index 2: ", list1[2])
list1[2] = 2001
print('new value is: ', list1[2])
del list1[2]
len(list1)

list4 = list(range(5))
print(len(list4))

aTuple = (123, 'c++', 'java', 'Python')
list1 = list(aTuple)
print("list", list1)

str = "Hello Benjamin"
list2 = list(str)
print("list", list2)

list1.append('c#')


aList = [123, 'xyz', 'zara', 'abc', 123]
print(aList.count(123))
print(aList.count('zara'))

list2.extend(aList)
print(list2)
list2.insert(1, 'Golang')
