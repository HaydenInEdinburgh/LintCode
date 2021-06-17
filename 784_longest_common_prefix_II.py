class Solution:
    """
    @param dic: the n strings
    @param target: the target string
    @return: The ans
    """
    def theLongestCommonPrefix(self, dic, target):
        # write your code here
        if not target or not dic:
            return 0

        maximum = 0
        for word in dic:
            if len(word) <= maximum:
                continue
            index = self.helper(target, word)
            print(word, index)
            maximum = max(index, maximum)

        return maximum

    def helper(self, prefix, word):
        n = min(len(prefix), len(word))
        for i in range(n):
            if prefix[i] != word[i]:
                return i
        return n
if __name__ == '__main__':
    s = Solution()
    dict = ["abcba","acc","abwsf"]
    target = "abse"
    s.theLongestCommonPrefix(dict, target)