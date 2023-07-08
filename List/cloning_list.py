# Using slicing
def Cloning(li1):
    li_copy = li1[:]
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


# Using append()
def Cloning(li1):
    li_copy = []
    for item in li1: li_copy.append(item)
    return li_copy

li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("\nOriginal List:", li1)
print("After Cloning:", li2)


# importing copy module
import copy
# initializing list 1
li1 = [1, 2, [3, 5], 4]
# using copy for shallow copy
li2 = copy.copy(li1)
print('\n', li2)