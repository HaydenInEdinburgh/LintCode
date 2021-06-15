class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def isPossible(self, nums):
        # write your code here
        if not nums:
            return False

        num_cnt = {}
        tails = {}
        for n in nums:
            num_cnt[n] = num_cnt.get(n, 0) + 1
            tails[n] = 0

        for num in nums:
            if num_cnt[num] == 0:
                continue

            if num-1 in tails and tails[num-1] > 0:
                tails[num-1] -= 1
                tails[num] += 1

            elif num+1 in num_cnt and num_cnt[num+1] and num+2 in num_cnt and num_cnt[num+2]:
                num_cnt[num+1] -= 1
                num_cnt[num+2] -= 1
                tails[num+2] += 1
            else:
                return False

            num_cnt[num] -= 1

        return True