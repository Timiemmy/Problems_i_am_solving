'''
Given a list of integers with duplicate elements in it.
The task is to generate another list, which contains only the duplicate elements.
'''

list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

uniqueList = []
duplicateList = []

for i in list:
    if i not in uniqueList:
        uniqueList.append(i)
    elif i not in duplicateList:
        duplicateList.append(i)

print(duplicateList)