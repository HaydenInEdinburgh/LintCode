class Solution:
    """
    @param s: the given expression
    @return: the result of expression
    """
    def calculate(self, s):
        # Write your code here
        if not s:
            return 0

        stack = []
        num = 0
        sign = '+'

        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            if (not c.isdigit() and not c.isspace()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                sign = c
                num = 0

        return sum(stack)

if __name__ == '__main__':
    s = Solution()
    input = "3+2*2"
    print(s.calculate(input))