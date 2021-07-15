class Solution:
    """
    @param nums1: an array
    @param nums2: an array
    @return:  find all the next greater numbers for nums1's elements in the corresponding places of nums2
    """
    def nextGreaterElement(self, nums1, nums2):
        # Write your code here
        if not nums1:
            return []

        idxs = {n: i for i, n in enumerate(nums2)}
        res = []
        for num in nums1:
            start = idxs[num] +1
            result = self.find_first_greater(start, num, nums2)
            res.append(result)

        return res

    def find_first_greater(self, start, target, nums):
        if start >= len(nums):
            return -1

        for i in range(start, len(nums)):
            if nums[i] > target:
                return nums[i]

        return -1

if __name__ == '__main__':
    s =Solution()
    nums1 = [4,1,2]
    nums2 = [1,3,4,2]
    print(s.nextGreaterElement(nums1, nums2))
