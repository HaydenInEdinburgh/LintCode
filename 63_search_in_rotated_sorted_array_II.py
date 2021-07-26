class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """
    def search(self, A, target):
        # write your code here
        for num in A:
            if num == target:
                return True
        return False

if __name__ == '__main__':
    nums = [9,5,6,7,8,9,9,9,9,9,9]
    target = 8
    s = Solution()
    print(s.search(nums, target))