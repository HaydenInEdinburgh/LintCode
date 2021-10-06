class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums:
            return None

        l, r = 0, len(nums)-1
        while l+1< r:
            mid = (l +r)//2
            if nums[l] > nums[r]:
                r = mid
            elif nums[mid] > nums[r]:
                l = mid
            else:
                r -= 1

        return min(nums[l], nums[r])
