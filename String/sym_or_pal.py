'''
Given a string. the task is to check if the string is symmetrical and palindrome or not.
'''

string = 'amaama'
half = int(len(string) / 2)

first_str = string[:half]
second_str = string[half:]

# symmetric
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')

# palindrome
if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')
