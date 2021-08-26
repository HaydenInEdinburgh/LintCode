class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: rotate the array to the right by k steps
    """
    def rotate(self, nums, k):
        # Write your code here
        if not nums:
            return []
        n = len(nums)
        if k >n:
            k %= n
        self.swap(nums, n-k, n-1)
        self.swap(nums, 0, n-k-1)
        self.swap(nums, 0, n-1)


    def swap(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums
if __name__ == '__main__':
    nums = [1,2,3,4,5,6]
    k = 11
    s = Solution()
    print(s.rotate(nums, k))