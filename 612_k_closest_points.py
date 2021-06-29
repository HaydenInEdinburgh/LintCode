"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def kClosest(self, points, origin, k):
        # write your code here
        if not points or not k:
            return []

        points_with_dis = [(self.cal_distance(p.x, p.y, origin), p) for p in points]
        sorted_points = sorted(points_with_dis, key=lambda p: [p[0], p[1].x, p[1].y])
        return [p for _, p in sorted_points[:k]]

    def cal_distance(self, x, y, origin):
        o_x, o_y = origin.x, origin.y
        return (x-o_x) ** 2 + (y-o_y) ** 2

if __name__ == '__main__':
    s = Solution()
    points = [[4,6],[4,7],[4,4],[2,5],[1,1]]
    origin = [0, 0]
    k = 3
    print(s.kClosest(points, k))