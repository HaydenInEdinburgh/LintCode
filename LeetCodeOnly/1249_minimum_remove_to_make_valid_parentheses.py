class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return ''
        stack = []
        toDelete = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append((i,char))
            elif char == ')':
                if len(stack) > 0:
                    stack.pop()
                else:
                    toDelete.append(i)

        for i, _ in stack:
            toDelete.append(i)

        chars = list(s)
        for i in toDelete:
            chars[i] = ''

        return ''.join(chars)

if __name__ == '__main__':
    s = Solution()
    input = "))(("
    print(s.minRemoveToMakeValid(input))