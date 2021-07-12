class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        if not A:
            return []
        self.merge_sort(A)

    def quick_sort(self, start, end, nums):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(start +end)//2]
        while left < right:
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


    def merge_sort(self, nums):
        if len(nums) <= 1:
            return
        mid = len(nums) //2
        # divide and conquer
        L, R = nums[:mid], nums[mid:]
        self.merge_sort(L)
        self.merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            nums[k] = L[i]
            k += 1
            i += 1
        while j < len(R):
            nums[k] = R[j]
            k += 1
            j += 1

if __name__ == '__main__':
    s = Solution()
    A = [3, 2, 1, 4, 5]
    s.sortIntegers2(A)
    print(A)