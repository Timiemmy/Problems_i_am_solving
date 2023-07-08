'''
Given a list of numbers, write a Python program to print all positive numbers in given list.
'''

list1 = [12, -7, 5, 64, -14, -95]
pos_num = []
neg_num = []
for i in list1:
    if i > 0:
        pos_num.append(i)
    else:
        neg_num.append(i)
print(pos_num,'\n''\t', neg_num)
