from typing import (
    List,
)

class Solution:
    """
    @param nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        # write your code here
        if not nums:
            return [[]]

        res = []
        visited = [False] * len(nums)
        self.dfs(nums, [], visited, res)

        return res

    def dfs(self, nums, path, visited, res):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i, n in enumerate(nums):
            if visited[i]:
                continue
            path.append(n)
            visited[i] = True
            self.dfs(nums, path, visited, res)
            visited[i] = False
            path.pop()

