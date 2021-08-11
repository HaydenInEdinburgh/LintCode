class Solution:
    """
    @param path: the original path
    @return: the simplified path
    """
    def simplifyPath(self, path):
        # write your code here
        if not path or path == '/':
            return ''

        stack = []
        dics = path.split('/')
        for p in dics:
            if p == '..':
                if stack:
                    stack.pop()
            elif p and p != '.':
                stack.append(p)

        return '/'+ '/'.join(stack)