class Solution:
    """
    @param nums: an array
    @return: the longest length of set S
    """
    def arrayNesting(self, nums):
        # Write your code here
        if not nums:
            return 0

        self.maxLen = 0
        visited = set()
        for n in nums:
            if n in visited:
                continue
            visited.add(n)
            self.helper(nums, n, [n], visited)

        return self.maxLen

    def helper(self, nums, start, path, visited):
        if nums[start] in visited or len(path) == len(nums):
            self.maxLen = max(self.maxLen, len(path))
            return
        path.append(nums[start])
        visited.add(nums[start])
        self.helper(nums, nums[start], path, visited)

class Solution2:
    def arrayNesting(self, nums):
        # Write your code here
        if not nums:
            return 0

        ans, step, n = 0, 0, len(nums)
        seen = [False] * n

        for i in range(n):
            while not seen[i]:
                seen[i] = True
                i = nums[i]
                step += 1
            ans = max(ans, step)
            step = 0

        return ans



if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2]
    print(s.arrayNesting(nums))