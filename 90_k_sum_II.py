class Solution:
    """
    @param A: an integer array
    @param k: a postive integer <= length(A)
    @param targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        if not A:
            return []

        nums = sorted(A)
        res = []
        self.dfs(nums, k, [], res, target, 0)
        return res

    def dfs(self, nums, k, path, res, target, startIndex):
        if k == 0 and target != 0:
            return

        if k == 0 and target == 0:
            res.append(path[:])
            return

        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.dfs(nums, k-1, path, res, target -nums[i], i+1)
            path.pop()

if __name__ == '__main__':
    s = Solution()
    input = [1,2,3,4]
    target = 5
    k = 2

    output = s.kSumII(input, k, target)
    print(output)
