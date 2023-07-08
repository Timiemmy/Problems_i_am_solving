'''
Given a list in Python and a number x, count the number of occurrences of x in the given list.
'''


def occurence(d_list, x):
    return d_list.count(x)



d_list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10

print(occurence(d_list, x))


def occurence1(d_list, x):
    occur = 0
    for i in d_list:
        if i == x:
            occur += 1

    return occur

d_list = [15, 6, 7, 10, 12, 20, 10, 28, 10]
x = 10

print(occurence1(d_list, x))
