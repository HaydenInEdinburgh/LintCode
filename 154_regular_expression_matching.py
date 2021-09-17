class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        return self.helper(s, 0, p, 0, {})

    def helper(self, source, i, pattern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(source) == i: #source reach the end
            return self.is_all_star(pattern, j) #if the left are all *
        if len(pattern) == j:#pattern reach the end but source not
            return False
        if j+1 < len(pattern) and pattern[j+1] == '*':
            matched = (self.char_match(source[i], pattern[j]) and self.helper(source, i+1, pattern, j, memo)) or self.helper(source, i, pattern, j+2, memo)
        else:
            matched = self.char_match(source[i], pattern[j]) and self.helper(source, i+1, pattern, j+1, memo)
        memo[(i, j)] = matched
        return matched

    def char_match(self, s, p):
        return s == p or p == '.'

    def is_all_star(self, p, j):
        for i in range(j, len(p), 2):
            print(i)
            if i+1 == len(p) or p[i+1] != '*':
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    input = ''
    print(s.is_all_star(input, 0))
