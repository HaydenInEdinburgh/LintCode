class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        if not nums:
            return 0
        cnt, prefix = 0, 0
        pre_cnt = {0: 1}
        for n in nums:
            prefix += n
            if prefix - k in pre_cnt:
                cnt += pre_cnt[prefix -k]
            pre_cnt[prefix] = pre_cnt.get(prefix, 0) + 1

        return cnt
if __name__ == '__main__':
    s = Solution()
    nums = [2,1,-1,1,2]
    k = 3
    print(s.subarraySumEqualsK(nums, k))