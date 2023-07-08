'''
Given a List. The task is to find the sum and average of the list.
'''

def sum_and_avg(d_list):
    count = sum(d_list)

    # finding average
    avg = count / len(d_list)

    print("sum = ", count)
    print("average = ", avg)



d_list = [4, 5, 1, 2, 9, 7, 10, 8]
sum_and_avg(d_list)