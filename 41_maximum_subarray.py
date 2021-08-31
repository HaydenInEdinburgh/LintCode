import sys


class Solution1:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        if not nums:
            return 0

        prefix, minimums = [], [0]
        tmp_sum = 0

        for n in nums:
            tmp_sum += n
            prefix.append(tmp_sum)
            minimums.append(min(minimums[-1], tmp_sum))
        # print(prefix)
        # print(minimums)
        res = - sys.maxsize
        for i in range(len(prefix)):
            res = max(res, prefix[i] - minimums[i])

        return res


class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        # prefix_sum记录前i个数的和，max_Sum记录全局最大值，min_Sum记录前i个数中0-k的最小值
        min_sum, max_sum = 0, -sys.maxsize
        prefix_sum = 0

        for num in nums:
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - min_sum)
            min_sum = min(min_sum, prefix_sum)

        return max_sum

if __name__ == '__main__':
    s = Solution() 
    nums = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
    print(s.maxSubArray(nums))