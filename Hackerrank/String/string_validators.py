'''
You are given a string .
Your task is to find out if the string  contains:
alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
In the second line, print True if  has any alphabetical characters. Otherwise, print False.
In the third line, print True if  has any digits. Otherwise, print False.
In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
'''


s = input()
print(any(a.isalnum() for a in s) )
print(any(a.isalpha() for a in s) )
print(any(a.isdigit() for a in s) )
print(any(a.islower() for a in s) )
print(any(a.isupper() for a in s) )