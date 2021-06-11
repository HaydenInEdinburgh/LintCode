class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """

    def expressionExpand(self, s):
        # write your code here
        if not s:
            return ''

        number_stack = []
        char_stack = ['']
        num = 0
        for char in s:
            #print(number_stack)
            #print(char_stack)
            if char.isdigit(): #chat to int is a important part here
                num = num * 10 + int(char)

            if char == '[':
                number_stack.append(num)
                num = 0
                char_stack.append('')
                continue

            if char == ']':
                tmp = number_stack.pop() * char_stack.pop()
                if not char_stack:
                    char_stack = ['']
                char_stack[-1] = char_stack[-1]+tmp

            if char.isalpha():
                char_stack[-1] = char_stack[-1] + char


        return ''.join(char_stack)

if __name__ == '__main__':
    s = Solution()
    input = '3[2[ad]3[pf]]xyz'
    print(s.expressionExpand(input))