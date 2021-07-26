class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binarySearch(self, nums, target):
        # write your code here
        n = len(nums)
        if not n: return -1

        l, r = 0, n-1
        while l+1 <r:
            mid = (l +r)//2
            if nums[mid] < target:
                l = mid
            else:
                r = mid

        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1

if __name__ == '__main__':
    nums = [1,4,4,5,7,7,8,9,9,10]
    target = 1
    s = Solution()
    print(s.binarySearch(nums, target))