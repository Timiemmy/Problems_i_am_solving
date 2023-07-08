'''
Given a list of numbers, the task is to write a Python program to find the second largest number in the given list.
'''

list1 = [10, 20, 4]
list2 = [70, 11, 20, 4, 100]
list2.remove(max(list2))
print(max(list2))