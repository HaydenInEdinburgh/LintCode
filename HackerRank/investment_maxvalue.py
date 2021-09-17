import itertools

class Solution:
    def maxValue(self, n, rounds):
        if not rounds or not n:
            return 0

        investments = [0] * (n+1)
        for start, end, amount in rounds:
            investments[start-1] += amount
            investments[end] -= amount
        print(investments)
        investments = itertools.accumulate(investments)
        return max(investments)

if __name__ == '__main__':
    s = Solution()
    n = 5
    rounds = [(1, 2, 100), (2, 5, 100), (3, 4, 100)]
    print(s.maxValue(n, rounds))