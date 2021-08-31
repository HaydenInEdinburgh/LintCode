class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        if not nums: return None

        left, right = 0, len(nums)-1

        while left + 1< right:
            mid = (left +right)//2
            if nums[mid] > nums[left]:
                if nums[mid] > nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                right = mid

        if nums[left] < nums[right]:
            return nums[left]
        return nums[right]

if __name__ == '__main__':
    s = Solution()
    nums = [3,4,5,1,2]
    print(s.findMin(nums))