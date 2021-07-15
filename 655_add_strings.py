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

class Solution_CharOnly:
    def addStrings(self, num1, num2):
        if not num1 and num2:
            return ""

        l, r = len(num1)-1, len(num2)-1
        carry = 0
        res = ""
        while l>= 0 or r>= 0 or carry:
            n_a = int(num1[l]) if l >=0 else 0
            n_b = int(num2[r]) if r >=0 else 0
            final = (n_a + n_b + carry) % 10
            carry = (n_a + n_b + carry) // 10
            res += str(final)
            l -= 1
            r -= 1

        return res[::-1]

if __name__ == '__main__':
    s = Solution_CharOnly()
    num1 = '123'
    num2 = '45'
    print(s.addStrings(num1, num2))
