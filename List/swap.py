'''
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
'''

def SwapList(d_list, pos1, pos2):

    temp = d_list[pos1]
    d_list[pos1] = d_list[pos2]
    d_list[pos2] = temp

    return d_list

d_list = [23, 65, 19, 90]
pos1 = 1
pos2 = 3

print(SwapList(d_list, pos1-1, pos2-1))