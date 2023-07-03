'''
Given a list, write a Python program to swap first and last element of the list.
'''

def swap(newlist):
    size = len(newlist)

    temp = newlist[0]
    newlist[0] = newlist[size - 1]
    newlist[size - 1] = temp

    return newlist

print('Add number and swap first number to the last. Type "done" when you are done')

newlist = []

while True:
    user = input('Add number: ')
    if user == 'done':
        break
    try:
        user=int(user)
        newlist.append(user)


    except ValueError:
        print('Please input only number')



print(swap(newlist))
