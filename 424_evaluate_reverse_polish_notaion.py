class Solution:
    """
    @param tokens: The Reverse Polish Notation
    @return: the value
    """
    def evalRPN(self, tokens):
        # write your code here
        #+, -, *, /
        if not tokens:
            return 0

        num_stack = []
        for ele in tokens:
            if ele.isdigit() or (len(ele) > 1 and ele.startswith('-')):
                num_stack.append(int(ele))
            elif len(num_stack) >= 2:
                b = num_stack.pop()
                a = num_stack.pop()
                if ele == "+":
                    num_stack.append(a+b)
                if ele == "-":
                    num_stack.append(a-b)
                if ele == "*":
                    num_stack.append(a*b)
                if ele == "/":
                    num_stack.append(int(a/b))

        return num_stack[0]

if __name__ == '__main__':
    input = ["3","-4","+"]
    s = Solution()
    print(s.evalRPN(input))