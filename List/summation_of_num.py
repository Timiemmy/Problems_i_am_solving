'''
finding the summation of digits of numbers
'''

test_list = [12, 67, 98, 34]

sec_list = []
for i in test_list:
    sum = 0
    for j in str(i):
        sum += int(j)
    sec_list.append(sum)

print(sec_list)
