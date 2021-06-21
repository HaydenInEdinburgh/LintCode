import heapq
class Solution:
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
