"""
In python, you can use list as stack
stack = [1,2,3,4]
Get top element: stack[-1]  -> 4
Pop element: stack.pop()   -> 4
Push element: stack.append(5)
check the size of stack: len(stack)
"""


class Solution:
    """
    @param: stk: an integer stack
    @return: void
    """
    def stackSorting(self, stk):
        # write your code here
        if not stk:
            return

        back_stack = []
        while stk:
            top = stk.pop()
            while back_stack and top > back_stack[-1]:
                stk.append(back_stack.pop())
            back_stack.append(top)

        while back_stack:
            stk.append(back_stack.pop())






if __name__ == '__main__':
    s = Solution()
    stk = [4, 2, 1, 3, 5]
    s.stackSorting(stk)