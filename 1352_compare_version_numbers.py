class Solution:
    """
    @param version1: the first given number
    @param version2: the second given number
    @return: the result of comparing
    """
    def compareVersion(self, version1, version2):
        # Write your code here
        if not version1 or not version2:
            return None

        nums_1, nums_2 = version1.split('.'), version2.split('.')
        l, r = 0, 0

        while l< len(nums_1) and r< len(nums_2):
            if int(nums_1[l]) > int(nums_2[r]):
                return 1
            if int(nums_1[l]) < int(nums_2[r]):
                return -1
            l += 1
            r += 1

        if l < len(nums_1) and self.check_zero(nums_1, l):
            return 1
        if r < len(nums_2) and self.check_zero(nums_2, r):
            return -1
        return 0

    def check_zero(self, arr, start):
        i = start
        while i < len(arr):
            if int(arr[i]) != 0:
                return True
            i += 1
        return False


if __name__ == '__main__':
    s = Solution()
    version1 = '0.1.0'
    version2 = '0.1.1'
    print(s.compareVersion(version1, version2))