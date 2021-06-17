class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """

    def longestCommonPrefix(self, strs):
        # write your code here
        if not strs:
            return ''

        prefix = strs[0]

        for i in range(1, len(strs)):
            if strs[i].startswith(prefix):
                continue
            index = self.helper(prefix, strs[i])
            if index == 0:
                return ''
            prefix = prefix[:index]

        return prefix

    def helper(self, prefix, word):
        n = min(len(prefix), len(word))

        for i in range(n):
            if prefix[i] != word[i]:
                return i

        return n

if __name__ == '__main__':
    s = Solution()
    strings = ["ABCD", "ABEF", "ABEF"]
    print(s.longestCommonPrefix(strings))