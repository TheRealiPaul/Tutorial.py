import random

list1 = []
for i in range(10):
    num = random.randint(3, 17)
    list1.append(num)

print("The first list is:", list1)

list2 = []
for num in list1:
    code = chr(num)
    list2.append(code)

print("The second list is:", list2)
