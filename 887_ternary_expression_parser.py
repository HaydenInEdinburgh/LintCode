class Solution:
    """
    @param expression: a string, denote the ternary expression
    @return: a string
    """
    def parseTernary(self, expression):
        # write your code here
        if not expression:
            return ""

        stack = []
        for c in expression[::-1]:
            if stack and stack[-1] == '?':
                stack.pop()
                left, right = stack.pop(), stack.pop()
                stack += (left if c == 'T' else right)
            elif c != ':':
                stack += c

        return stack[-1]

if __name__ == '__main__':
    s = Solution()
    exp = 'F?1:T?3:1'
    print(s.parseTernary(exp))