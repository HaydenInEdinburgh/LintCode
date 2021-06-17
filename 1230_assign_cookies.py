class Solution:
    """
    @param g: children's greed factor
    @param s: cookie's size
    @return: the maximum number
    """
    def findContentChildren(self, g, s):
        # Write your code here
        if not s or not g:
            return 0

        sorted_g = sorted(g)
        sorted_s = sorted(s)

        res = 0
        i, j = 0, 0
        while i < len(g) and j < len(s):
            if sorted_s[j] >= sorted_g[i]:
                res += 1
                i += 1
                j += 1
            else:
                j += 1

        return res

if __name__ == '__main__':
    solution = Solution()
    g = [1, 2, 3]
    s = [1, 2]
    print(solution.findContentChildren(g, s))