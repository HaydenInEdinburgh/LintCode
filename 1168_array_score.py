class Solution:
    """
    @param nums: the array to be scored.
    @param k: the requirement of subarray length.
    @param u: if the sum is less than u, get 1 score.
    @param l: if the sum is greater than l, lose 1 score.
    @return: return the sum of scores for every subarray whose length is k.
    """
    def arrayScore(self, nums, k, ue, le):
        # write your code here.
        if not nums:
            return 0

        l, r = 0, 0
        curSum = 0
        score = 0

        while r < len(nums):
            length = r-l
            if length <k:
                curSum += nums[r]
            elif length == k:
                #calculate score
                if curSum < ue:
                    score += 1
                if curSum > le:
                    score -= 1
                curSum += nums[r]
                curSum -= nums[l]
                l += 1
            r += 1

        if curSum < ue:
            score += 1
        if curSum > le:
            score -= 1

        return score

if __name__ == '__main__':
    s = Solution()
    nums = [0, 1, 2, 3, 4]
    k = 2
    u = 2
    l = 5
    print(s.arrayScore(nums, k, u, l))