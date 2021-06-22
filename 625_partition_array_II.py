class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums, low, high):
        # write your code here
        if not nums:
            return

        start = self.quick_select(nums, 0, len(nums)-1, low)
        self.quick_select_2(nums, start + 1, len(nums)-1, high)

    def quick_select(self, nums, start, end, pivot):
        if start == end:
            return start

        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] >= pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return right

    def quick_select_2(self, nums, start, end, pivot):
        if start == end:
            return start

        left, right = start, end
        while left <= right:
            while left <= right and nums[left] <= pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left