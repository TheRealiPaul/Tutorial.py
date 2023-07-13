list2 = [[24, 5, 9, 6], [55, 61, 32]]

list3 = [123, "group", 45, 56, "student", 70]
print(list3)
for item in list3:
    if str(item).isnumeric():
        print("result :", item * 2)

list4 = [["lobby", 5, 3], ["room1", 5, 3], ["room2", 5, 3]]
print(list4)
for i in list4:
    print(i, "area :", i[1] * i[2])

list5 = []
for x in range(3):
    sublist = []
    sublist.append(input("Room name: "))
    sublist.append(float(input("dimension: ")))
    sublist.append(float(input("dimension 2: ")))
    list5.append(sublist)
print(list5)
