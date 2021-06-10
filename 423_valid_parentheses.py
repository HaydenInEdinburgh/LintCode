class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """

    def isValidParentheses(self, s):
        # write your code here
        if not s:
            return True

        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False

                left = stack.pop()
                if char != mapping[left]:
                    return False

        return len(stack) == 0

if __name__ == '__main__':
    s = Solution()
    input = "]"
    print(s.isValidParentheses(input))