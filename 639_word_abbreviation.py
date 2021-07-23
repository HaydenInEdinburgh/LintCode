class Solution:
    """
    @param dict: an array of n distinct non-empty strings
    @return: an array of minimal possible abbreviations for every word
    """
    def wordsAbbreviation(self, dict):
        # write your code here
        n = len(dict)
        prefix = [1] * n
        abb_cnt = {}
        ans = []

        for i in range(n):
            word = dict[i]
            abb = self.get_abbr(word, prefix[i])
            ans.append(abb)
            abb_cnt[abb] = abb_cnt.get(abb, 0) + 1

        while True:
            unique = True
            for i in range(n):
                if abb_cnt[ans[i]] > 1:
                    prefix[i] += 1
                    new_abb = self.get_abbr(dict[i], prefix[i])
                    ans[i] = new_abb
                    abb_cnt[new_abb] = abb_cnt.get(new_abb, 0) +1
                    unique = False
            if unique:
                break

        return ans

    def get_abbr(self, word, prefix):
        if prefix >= len(word) -2:
            return word

        left, right = word[:prefix], word[-1]
        number = len(word) - prefix -1
        abbr = left + str(number) + right

        return abbr
