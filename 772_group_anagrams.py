class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        # write your code here
        if not strs: return []

        res = {}

        for word in strs:
            pin = ''.join(sorted(word))
            # print(word, pin)
            if pin not in res:
                res[pin] = []
            res[pin].append(word)

        return res.values()

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    s = Solution()
    print(s.groupAnagrams(strs))