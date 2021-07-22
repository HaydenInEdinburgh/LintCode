import heapq


class Solution:
    """
    @param nums: the array
    @return: the third maximum number in this array
    """
    def thirdMax(self, nums):
        # Write your code here.
        if len(nums) < 3:
            return max(nums)

        stack = []
        visited = set()
        for n in nums:
            if n in visited:
                continue
            visited.add(n)
            if len(stack) < 3:
                heapq.heappush(stack, n)
            else:
                if n > stack[0]:
                    heapq.heapreplace(stack, n)

        if len(visited) < 3:
            return stack[-1]
        return heapq.heappop(stack)

if __name__ == '__main__':
    s = Solution()
    num = [1, 2, 3, 2]
    print(s.thirdMax(num))