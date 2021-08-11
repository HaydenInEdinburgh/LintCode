class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def findMissing(self, nums):
        # write your code here
        n = len(nums)
        ori = (1 + n)*n/2
        return int(ori - sum(nums))
