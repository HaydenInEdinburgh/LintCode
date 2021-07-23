import heapq
class Solution:
    """
    @param num: a number
    @param k: the k digits
    @return: the smallest number
    """
    def removeKdigits(self, num, k):
        # write your code here.
        if not num:
            return ""

        num_stack = []
        for n in num:
            while k and num_stack and num_stack[-1] > n:
                num_stack.pop()
                k -= 1
            num_stack.append(n)
        # print(num_stack, k)
        num_stack = num_stack[:-k] if k else num_stack
        if not num_stack:
            return '0'
        return str(int(''.join(num_stack)))

if __name__ == '__main__':
    s = Solution()
    num = "637824056"
    k = 8
    print(s.removeKdigits(num, k))