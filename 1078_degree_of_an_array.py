class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findShortestSubArray(self, nums):
        # write your code here
        if not nums:
            return []

        ele_indices = {}
        for i, n in enumerate(nums):
            if n not in ele_indices:
                ele_indices[n] = []
            ele_indices[n].append(i)

        max_degree = max([len(arr) for arr in ele_indices.values()])
        res = len(nums)
        for _, arr in ele_indices.items():
            cur_len = arr[-1] - arr[0] +1 if len(arr) >1 else 1
            if len(arr) == max_degree:
                res = min(res, cur_len)

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 3, 1]
    print(s.findShortestSubArray(nums))