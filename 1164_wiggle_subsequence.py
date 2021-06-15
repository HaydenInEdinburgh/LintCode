class Solution:
    """
    @param nums: the given sequence
    @return: the length of the longest subsequence that is a wiggle sequence
    """
    def wiggleMaxLength(self, nums):
        # Write your code here
        if not nums:
            return 0

        inc_len, dec_len = 0, 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                inc_len = dec_len +1
            elif nums[i] > nums[i-1]:
                dec_len = inc_len +1

        return max(inc_len, dec_len)