class Solution:
    """
    @param nums: an array
    @return: the number occurs twice and the number that is missing
    """
    def findErrorNums(self, nums):
        # Write your code here
        if not nums:
            return

        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n, 0) +1
        print(cnt)

        lost, dup = None, None
        for i in range(1, len(nums)+1):
            if i not in cnt:
                lost = i
                continue
            if cnt[i] > 1:
                dup = i

        return [dup, lost]


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1]
    print(s.findErrorNums(nums))