class Solution:
    def minOperations(self, s: str) -> int:
        if not s:
            return 0

        sol1 = 0
        for i, char in enumerate(s):
            if i %2 ==0 and char == '1':
                sol1 += 1
            if i %2 ==1 and char == '0':
                sol1 += 1

        return min(len(s)-sol1, sol1)