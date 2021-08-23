class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # write your code here
        if not heights:
            return 0
        n = len(heights)
        l, r = 0, n-1
        res = 0
        while l < r:
            area = (r -l) * min(heights[r], heights[l])
            res = max(res, area)
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return res

if __name__ == '__main__':
    s = Solution()
    heights = [1,2,1]
    print(s.maxArea(heights))