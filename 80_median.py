class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        # write your code here
        if not nums:
            return

        n = len(nums)
        return self.quick_select(nums, 0, n - 1, (n-1)//2)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]

        left, right = start, end
        pivot = nums[(left + right)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if k <= right:
            return self.quick_select(nums, start, left, k)
        if k > left:
            return self.quick_select(nums, right, end, k)
        return nums[k]

if __name__ == '__main__':
    s = Solution()
    nums = [4,5,1,2]
    print(s.median(nums))