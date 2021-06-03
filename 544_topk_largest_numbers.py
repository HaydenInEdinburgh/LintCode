class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # write your code here
        if not nums or not k:
            return []

        small_k = len(nums) -k
        kth = self.partition(nums, 0, len(nums)-1, small_k)

        return sorted([n for n in nums if n >= kth], reverse= True)

    def partition(self, nums, start, end, k):
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
            self.partition(nums, start, right, k)

        if k >= left:
            self.partition(nums, left, end, k)

        return nums[k]

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,4,2]
    k = 1
    print(s.topk(nums, k))