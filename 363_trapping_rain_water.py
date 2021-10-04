class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    # 每个位置上的盛水数目 = min(左侧最高，右侧最高) - 当前高度
    def trapRainWater(self, heights):
        # write your code here
        # water_added = min(left highest, right highest) - height
        n = len(heights)
        left_highest, height = [], 0
        for i in range(n):
            height = max(heights[i], height)
            left_highest.append(height)

        right_highest, height = [], 0
        for i in range(n - 1, -1, -1):
            height = max(heights[i], height)
            right_highest.append(height)
        right_highest = right_highest[::-1] #remember to reverse it
        water = 0
        for i in range(n):
            water += (min(left_highest[i], right_highest[i]) - heights[i])

        return water

if __name__ == '__main__':
    s = Solution()
    input = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trapRainWater(input))