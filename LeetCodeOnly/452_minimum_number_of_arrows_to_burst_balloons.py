class Solution:
    def findMinArrowShots(self, points) -> int:
        if not points:
            return 0

        res = 1
        sorted_points = sorted(points)
        end = sorted_points[0][1]

        for i in range(1, len(sorted_points)):
            cur_start, cur_end = sorted_points[i]
            if cur_start <= end:
                end = min(cur_end, end)
            else:
                # shot
                res += 1
                end = cur_end

        return res

if __name__ == '__main__':
    s = Solution()
    input = [[1,2],[2,4],[5,6],[6,8]]
    print(s.findMinArrowShots(input))