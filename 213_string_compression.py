class Solution:
    """
    @param originalString: a string
    @return: a compressed string
    """
    def compress(self, originalString):
        # write your code here
        if not originalString:
            return ""

        left, right = 0, 0
        n = len(originalString)
        res = ""
        while left < n:
            if right >= n or originalString[left] != originalString[right]:
                cnt = str(right -left)
                char = originalString[left]
                res = res + char + cnt
                left = right
            right += 1

        if len(res) >= n:
            return originalString
        return res
if __name__ == '__main__':
    s = Solution()
    original = "aabccaa"
    print(s.compress(original))