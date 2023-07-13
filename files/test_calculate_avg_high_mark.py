myList = []
sumGrades = 0

nbGrades = int(input("Please enter the number of students: "))

for i in range(nbGrades):
    grade = float(input("Please enter a grade between 0 and 100: "))
    if grade >= 0 and grade <= 100:
        myList.append(grade)
    else:
        print("Error!!! Invalid grade.")

print("Grades list:", myList)

highestGrades = []
for grade in myList:
    if grade >= 60 and grade <= 100:
        highestGrades.append(grade)

print("Highest grades in the group:", highestGrades)

sumGrades = sum(myList)
average = sumGrades / len(myList)
print("Group average:", average)

highestMark = max(myList)
print("Highest mark in the class:", highestMark)

countHighestGrade = myList.count(highestMark)
print("Number of students with the highest grade:", countHighestGrade)
