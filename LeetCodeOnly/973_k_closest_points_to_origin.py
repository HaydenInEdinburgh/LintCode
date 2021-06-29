import math

class Solution:
    def kClosest(self, points, k: int):
        if not points or not k:
            return []

        points_with_dis = [(self.cal_distance(x, y), x, y) for x, y in points]
        sorted_points = sorted(points_with_dis, key=lambda p: [p[0], p[1], p[2]])
        return [[x, y] for _, x, y in sorted_points[:k]]

    def cal_distance(self, x, y):
        return x**2 + y**2

if __name__ == '__main__':
    s = Solution()
    points = [[3,3],[5,-1],[-2,4]]
    k = 2
    print(s.kClosest(points, k))