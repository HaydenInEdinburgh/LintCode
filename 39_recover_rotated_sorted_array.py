class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if not nums: return []
        self.quick_sort(0, len(nums)-1, nums)
        return nums

    def quick_sort(self, start, end, nums):
        if start > end:
            return
        left, right = start, end
        pivot = nums[(left+right)//2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(start, right, nums)
        self.quick_sort(left, end, nums)


class Solution2:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        if not n: return []

        point = None
        for i in range(1, n):
            if nums[i] < nums[i-1]:
                point = i
                break

        if point:
            return nums[point:]+nums[:point]
        return nums



if __name__ == '__main__':
    s = Solution2()
    nums = [4,5,1,2,3]
    print(s.recoverRotatedSortedArray(nums))