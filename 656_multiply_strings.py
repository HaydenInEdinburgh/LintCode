class Solution:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        # write your code here
        if not num1 or not num2:
            return None

        digits = {str(d): d for d in range(10)}

        num1_val = 0
        for i in range(len(num1)-1, -1, -1):
            digit = digits[num1[i]]
            num1_val += digit * (10 ** (len(num1) - 1 - i))

        num2_val = 0
        for j in range(len(num2)-1, -1, -1):
            digit = digits[num2[j]]
            num2_val += (digit * (10 ** (len(num2) - 1 - j)))
        print(num1_val, num2)
        return str(num1_val * num2_val)

class Solution_better:
    """
    @param num1: a non-negative integers
    @param num2: a non-negative integers
    @return: return product of num1 and num2
    """
    def multiply(self, num1, num2):
        if num1 == '0' or num2 == '0': return '0'

        n = len(num1) + len(num2)
        res = [0] * n

        # cal
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                res[i + j + 1] += (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))

        # format
        for i in range(len(res)-1, 0, -1):
            res[i-1] += res[i] // 10
            res[i] = res[i] % 10

        ans = ''
        for i in range(len(res)):
            if not res[i] and not ans:
                continue
            ans += str(res[i])

        return ans

if __name__ == '__main__':
    s = Solution_better()
    n1 = '123'
    n2 = '45'
    print(s.multiply(n1, n2))