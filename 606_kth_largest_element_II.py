import heapq
class Solution_heap:
    """
    @param nums: an integer unsorted array
    @param k: an integer from 1 to n
    @return: the kth largest element
    """
    def kthLargestElement2(self, nums, k):
        # write your code here
        if not nums or len(nums) < k:
            return None

        maxheap = []
        for n in nums:
            heapq.heappush(maxheap, n)
            if len(maxheap) > k:
                heapq.heappop(maxheap)

        return heapq.heappop(maxheap)

class Solution_quick_select:
    def kthLargestElement2(self, nums, k):
        # write your code here
        if not nums or len(nums) < k:
            return None

        return self.quick_select(nums, 0, len(nums)-1, len(nums)-k)

    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[k]

        left, right = start, end
        pivot = nums[(left + right) // 2]

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
            return self.quick_select(nums, start, right, k)

        if k >= left:
            return self.quick_select(nums, left, end, k)

        return nums[k]

if __name__ == '__main__':
    s = Solution_quick_select()
    nums = [9,3,2,4,8]
    k = 3
    print(s.kthLargestElement2(nums, k))