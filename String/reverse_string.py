'''
We are given a string and we need to reverse words of a given string
'''

string = "geeks quiz practice code"

list = string.split()
new_string = ' '.join(list[::-1])

print(new_string)