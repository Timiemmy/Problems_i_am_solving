'''
removing the ith character from a string
'''

test_str = "GeeksForGeeks"

num = 2

def remove_from_string(str, num):
    li = []
    for i in str:
        li.append(i)
    remove = li.pop(num)
    new_str = ' '.join(li)
    return new_str

print(remove_from_string(test_str, num))