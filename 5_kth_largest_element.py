class Solution:
    """
    @param k: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, k, nums):
        # write your code here
        if not k or not nums: return None

        self.quick_sort(0, len(nums)-1, nums)
        print(nums)
        return nums[k-1]

    def quick_sort(self, start, end, nums):
        if start >= end:
            return

        left, right = start, end
        p = nums[(start +end)//2]
        while left < right:
            while left <= right and nums[left] > p:
                left += 1
            while left <= right and nums[right] <p:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quick_sort(start, right, nums)
        self.quick_sort(left, end, nums)

class Solution_Partition:
    def kthLargestElement(self, k, A):
        if not A or k < 1 or k > len(A):
            return None
        return self.partition(A, 0, len(A) - 1, len(A) - k)

    def partition(self, nums, start, end, k):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(left +right)//2]
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
            self.partition(nums, start, right, k)
        if k >= left:
            self.partition(nums, left, end, k)

        return nums[k]

if __name__ == '__main__':
    s = Solution_Partition()
    nums = [9, 5, 4, 3, 1, 7, 6]
    print(s.kthLargestElement(3, nums))