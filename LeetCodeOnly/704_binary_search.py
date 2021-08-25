class Solution:
    def search(self, nums, target: int) -> int:
        if not nums:
            return -1
        nums_with_idx = sorted([(v, i) for i, v in enumerate(nums)])
        l, r = 0, len(nums)-1
        while l+1 <r:
            mid = (l+r)//2
            num = nums_with_idx[mid][0]
            if num < target:
                l = mid
            elif num > target:
                r = mid
            else:
                return nums_with_idx[mid][1]

        if nums_with_idx[l][0] == target:
            return nums_with_idx[l][1]
        if nums_with_idx[r][0] == target:
            return nums_with_idx[r][1]
        return -1

