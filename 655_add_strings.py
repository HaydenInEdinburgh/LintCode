class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return sum of num1 and num2
    """
    def addStrings(self, num1, num2):
        # write your code here
        if not num1 and num2: return None

        digits = {str(d): d for d in range(10)}

        cur_sum = 0

        for i in range(len(num1)-1, -1, -1):
            char = num1[i]
            digit = digits[char]
            cur_sum += digit * (10 ** (len(num1) - 1 - i))

        for i in range(len(num2) - 1, -1, -1):
            char = num2[i]
            digit = digits[char]
            cur_sum += digit * (10 ** (len(num2) - 1 - i))

        return str(cur_sum)

if __name__ == '__main__':
    s = Solution()
    num1 = '123'
    num2 = '45'
    print(s.addStrings(num1, num2))
