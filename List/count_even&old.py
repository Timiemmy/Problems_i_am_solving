'''
Given a list of numbers, write a Python program to count Even and Odd numbers in a List.
'''

list1 = [2, 7, 5, 64, 14]

Even = 0
Odd = 0

for i in list1:
    if i % 2 == 0:
        Even += 1
    else:
        Odd += 1

print(f'We have {Even} even number, and {Odd} odd numbers')