class Solution:
    """
    @param s: A string with lowercase letters and parentheses
    @return: A string which has been removed invalid parentheses
    """
    def removeParentheses(self, s: str) -> str:
        # write your code here.
        if not s:
            return ''

        stack = []
        todelete = set()
        for i, char in enumerate(list(s)):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if not stack:
                    todelete.add(i)
                else:
                    stack.pop()

        while stack:
            todelete.add(stack.pop())

        return ''.join([char for i, char in enumerate(list(s)) if i not in todelete])

if __name__ == '__main__':
    s = Solution()
    string = "a(b(c(de)fgh)"
    print(s.removeParentheses(string))