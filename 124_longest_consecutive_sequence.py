class Solution:
    """
    @param num: A list of integers
    @return: An integer

    Your algorithm should run in O(n) complexity.
    len(num) <= 10000
    """
    def longestConsecutive(self, num):
        # write your code here
        if not num:
            return 0

        num = sorted(num)
        l, r = 0, 1
        res = 1
        while r < len(num):
            if num[r] == num[r-1]+1:
                r += 1
            else:
                print(num[r], num[l])
                res = max(res, num[r-1] - num[l] + 1)
                l = r
                r += 1
            while r < len(num) and num[r] == num[r-1]:
                r += 1

        res = max(res, num[r-1] - num[l] + 1)

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [101, 1, 2, 0, 1]
    print(s.longestConsecutive(nums))