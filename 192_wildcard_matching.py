class Solution:
    """
    @param s: A string
    @param p: A string includes "?" and "*"
    @return: is Match?
    """
    def isMatch(self, s, p):
        # write your code here
        return self.helper(s, 0, p, 0, {})

    def helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(source) == i:
            return self.is_all_star(pattern, j)

        if len(pattern) == j:#pattern has ran out
            return False

        if pattern[j] != '*':
            matched = self.char_match(source[i], pattern[j]) and self.helper(source, i+1, pattern, j+1, memo)

        else:
            matched = self.helper(source, i+1, pattern, j, memo) or self.helper(source, i, pattern, j+1, memo)
        memo[(i, j)] = matched

        return matched

    def is_all_star(self, p, j):
        for i in range(j, len(p)):
            if p[i] != '*':
                return False
        return True

    def char_match(self, s, p):
        return s == p or p == '?'