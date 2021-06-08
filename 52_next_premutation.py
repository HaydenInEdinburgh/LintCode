class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        if len(nums) <= 1:
            return nums

        for i in range(len(nums)-1, -1, -1):
            if i >0 and nums[i-1] < nums[i]:
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        #swap
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        left, right = i, len(nums)-1
                        while left <= right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1
                        return nums

        nums.reverse()
        return nums



if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([1, 1, 2]))