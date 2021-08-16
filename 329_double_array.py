class Solution:
    """
    @param arr: a positive integer array
    @param num: a positive integer
    @return: return the maxium num
    """
    def maxNum(self, arr, num):
        # write your code here
        if not arr:
            return num

        res = num
        for n in arr:
            if n == res:
                res *= 2

        return res
