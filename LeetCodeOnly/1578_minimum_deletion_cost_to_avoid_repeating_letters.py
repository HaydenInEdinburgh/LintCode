class Solution:
    def minCost(self, s: str, cost) -> int:
        if not s or len(s) == 1:
            return 0

        total = 0
        left, right = 0, 1

        while right < len(s):
            if not s[left] == s[right]:
                left = right
                right += 1
                continue

            if cost[left] <= cost[right]:
                total += cost[left]
                left = right
                right += 1
            else:
                total += cost[right]
                right += 1

        return total

if __name__ == '__main__':
    slt = Solution()
    s = "aabaa"
    cost = [1, 2, 3, 4, 1]
    print(slt.minCost(s, cost))