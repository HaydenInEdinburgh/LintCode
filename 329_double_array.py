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
        arr.sort()

        for n in arr:
            if n == num:
                num *= 2

        return num
