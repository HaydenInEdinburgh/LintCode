class Solution:
    """
    @param nums: an integer array.
    @return: return the possible longest length of the subarray that elements are the same.
    """
    def threeChances(self, nums):
        # write your code here.
        n = len(nums)
        if n <= 3: return n
        l = r = 0 #arr = nums[l:r]
        res = 0
        cnt = {}
        while r < n:
            r_char = nums[r]
            cnt[r_char] = cnt.get(r_char, 0) +1
            r += 1
            while not self.valid(cnt, r-l):
                l_char = nums[l]
                cnt[l_char] -= 1
                l += 1
            res = max(res, r-l)

        return res

    def valid(self, cnt, length):
        if len(cnt) == 0:
            return True
        max_cnt = max(cnt.values())
        if length - max_cnt <= 3:
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,1,0,1,0,1,0]
    print(s.threeChances(nums))
