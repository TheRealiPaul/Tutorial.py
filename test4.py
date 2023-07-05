import random

randomList = []
newList = []

# Generate and display the two lists: randomList and newList
for i in range(10):
    r = random.randint(0, 255)
    randomList.append(r)
    newList.append(chr(r))

# Print the lists
print("The random list is:", randomList)
print("The new list is:", newList)
