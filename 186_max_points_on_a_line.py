"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param points: an array of point
    @return: An integer
    """
    def maxPoints(self, points):
        # write your code here
        if not points:
            return 0

        maximum = 0
        for i in range(len(points)):
            cur = self.cal_helper(i, points)# use ith point as the center
            maximum = max(maximum, cur)

        return maximum+1

    def cal_helper(self, base_i, points):
        base = points[base_i]
        map = {}
        res = 0
        for i in range(len(points)):
            if i == base_i:
                continue
            k = self.locator(base, points[i])
            map[k] = map.get(k, 0) + 1
            res = max(res, map[k])
        #print(map)
        return res

    def locator(self, p_a, p_b):
        k = (p_b[1] - p_a[1])/(p_b[0] - p_a[0]) if p_b[0] != p_a[0] else float('inf')
        #print(p_a, p_b, k)
        return k

    # def locator(self, p_a, p_b):
    #     k = (p_b.y - p_a.y)/(p_b.x - p_a.x) if p_b.x != p_a.x else float('inf')
    #     return k

if __name__ == '__main__':
    points = [[0,0],[1,1],[1,-1]]
    s = Solution()
    print(s.maxPoints(points))
