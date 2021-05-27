class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        if not nums:
            return [[]]

        numbers = sorted(nums)
        res = []
        self.dfs(numbers, res, [], 0)

        return res

    def dfs(self, numbers, res, path, startIndex):
        res.append(path[:])
        for i in range(startIndex, len(numbers)):
            path.append(numbers[i])
            self.dfs(numbers, res, path, i+1)
            path.pop()

if __name__ == '__main__':
    input = [1, 2]
    s = Solution()
    output = s.subsets(input)
    print(output)