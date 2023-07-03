class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:  # continue adding digits until we get a single-digit number
            sum_of_digits = 0
            while num > 0:
                sum_of_digits += num % 10  # add the last digit of num to sum_of_digits
                num //= 10  # remove the last digit from num
            num = sum_of_digits  # update num to the sum of its digits
        return num  # return the final single-digit number


num1 = Solution()

print(num1.addDigits(34))