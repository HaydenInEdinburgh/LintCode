import math


class Solution:
    """
    @param points: a 2D array
    @return: the number of boomerangs
    """

    def numberOfBoomerangs(self, points):
        # Write your code here
        n = len(points)
        if n < 3: return 0
        distance = {(x, y): {} for x,y in points}

        for i in range(n):
            p1 = points[i]
            for j in range(i+1, n):
                p2 = points[j]
                self.get_distance(distance, p1, p2)

        res = 0
        for _, p_distance in distance.items():
            for _, p_num in p_distance.items():
                if p_num >= 2:
                    res += (p_num * (p_num-1))

        return res

    def get_distance(self, distance, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        dis = (x1 - x2) ** 2 + (y1 - y2) ** 2

        distance[(x1, y1)][dis] = distance[(x1, y1)].get(dis, 0) +1
        distance[(x2, y2)][dis] = distance[(x2, y2)].get(dis, 0) +1

if __name__ == '__main__':
    s = Solution()
    points = [[0,0],[1,0],[2,0]]
    print(s.numberOfBoomerangs(points))