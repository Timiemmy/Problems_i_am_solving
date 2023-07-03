'''
In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.

The first line of input contains the original string. The next line contains the substring.

Sample Input
ABCDCDC
CDC
'''

# Using while loop
def count_substring(string, sub_string):
    counting = 0
    while sub_string in string:
        a = string.find(sub_string)
        string = string[a + 1:]
        counting += 1
    return counting


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


# Using for loop
def count_substring(string, sub_string):
    return sum(string[i:].startswith(sub_string) for i in range(len(string)))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

# Using If condition
c = 0
def count_substring(string, sub_string):
    global c
    if (string.find(sub_string) != -1):
        c = c + 1
        count_substring(string[string.find(sub_string) + 1:], sub_string)
    return c


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)