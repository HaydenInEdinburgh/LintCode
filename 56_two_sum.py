class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        if not numbers:
            return []

        nums = [(n, index) for index, n in enumerate(numbers)]
        nums.sort()

        left, right = 0, len(nums)-1
        while left < right:
            tmp_sum = nums[left][0] + nums[right][0]
            if tmp_sum == target:
                return sorted([nums[left][1], nums[right][1]])
            if tmp_sum < target:
                left += 1
            else:
                right -= 1

        return []