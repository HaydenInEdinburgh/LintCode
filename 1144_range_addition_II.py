class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param ops: List[List[int]]
    @return: return an integer
    """
    def maxCount(self, m, n, ops):
        # write your code here
        if not m or not n:
            return 0

        min_x, min_y = m, n
        for a, b in ops:
            min_x = min(min_x, a)
            min_y = min(min_y, b)

        return min_y * min_x