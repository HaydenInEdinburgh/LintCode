class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        if not s:
            return 0

        res = 0
        stack = []
        sign = 1
        number = 0

        for char in s:
            if char in '1234567890':
                number = number * 10 + int(char)
            elif char == '+':
                res += sign * number
                number = 0
                sign = 1
            elif char == '-':
                res += sign * number
                number = 0
                sign = -1
            elif char == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif char == ')':
                res += number * sign
                number = 0
                res *= stack[-1]
                res += stack[-2]
                stack = stack[:-2]
        res += sign * number
        return res

if __name__ == '__main__':
    s = Solution()
    input = "2-4-(8+2-6+(8+4-(1)+8-10))"
    print(s.calculate(input))
