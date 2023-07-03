class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0

        for i in range(len(s) - 1, -1, -1):
            current_value = roman_numerals[s[i]]
            if current_value < prev_value:
                result -= current_value
            else:
                result += current_value
            prev_value = current_value

        return result


rom = Solution()
print(rom.romanToInt('MDLV'))

'''
Here's a breakdown of each component of the code:

roman_numerals = { ... } : This line defines a dictionary called roman_numerals that maps 
Roman numeral characters to their corresponding decimal values. 
For example, the letter 'I' maps to the value 1.

result = 0 : This line initializes a variable called result to 0. 
We will add up the decimal values of the Roman numeral characters to this variable.

prev_value = 0 : This line initializes a variable called prev_value to 0. 
We will use this variable to keep track of the value of the previous Roman numeral character that we processed.

for i in range(len(s)-1, -1, -1): : This line starts a for loop that iterates over the characters of the input string s, 
starting from the last character and moving backwards to the first character. 
We use the range function to specify the starting and ending indices of the loop, as well as the step size.

current_value = roman_numerals[s[i]] : This line looks up the decimal value of the current Roman numeral character by 
indexing the roman_numerals dictionary using the current character.

if current_value < prev_value: ... else: ... : This line checks whether the current value is less than the previous value. 
If it is, we subtract the current value from the result. Otherwise, we add the current value to the result.

prev_value = current_value : This line updates prev_value to be the current value, 
so that we can compare it to the next character in the next iteration of the loop.

return result : This line returns the final value of result, which represents the decimal value of the input Roman numeral.
'''