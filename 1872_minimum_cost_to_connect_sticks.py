import heapq
class Solution:
    """
    @param sticks: the length of sticks
    @return: Minimum Cost to Connect Sticks
    """
    def MinimumCost(self, sticks):
        # write your code here
        if not sticks: return 0

        heapq.heapify(sticks)
        cost = 0

        while len(sticks) > 1:
            a = heapq.heappop(sticks)
            b = heapq.heappop(sticks)
            cost += (a + b)
            heapq.heappush(sticks, a+b)

        return cost

if __name__ == '__main__':
    s = Solution()
    sticks = [2,4,3]
    print(s.MinimumCost(sticks))