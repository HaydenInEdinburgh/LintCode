class Solution:
    """
    @param points: List[List[int]]
    @return: return a double
    """
    def largestTriangleArea(self, points):
        # write your code here
        n = len(points)
        if n < 3:
            return None
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for h in range(j+1, n):

                    area = self.cal_area(points, i, j, h)
                    #print(area)
                    res = max(res, area)

        return res

    def cal_area(self, points, a, b, c):
        x_a, y_a = points[a]
        x_b, y_b = points[b]
        x_c, y_c = points[c]

        return abs((x_a * y_b + x_b * y_c + x_c * y_a - x_a * y_c - x_b * y_a - x_c * y_b) /2)

if __name__ == '__main__':
    s = Solution()
    points = [[4,6],[6,5],[3,1]]
    print(s.largestTriangleArea(points))
