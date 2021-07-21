"""
Give a string s which represents the content of the novel,
and then give a list indicating that the words do not participate in statistics,
find the most frequent word(return the one with the smallest lexicographic order
if there are more than one word)
"""

class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        # Write your code here
        if not s:
            return ""

        ex_word = set(excludewords)
        s = ''.join(e for e in s if e.isalnum() or e == ' ')
        words_in_novel = s.split(' ')
        words_cnt = {}

        max_time, most_frequent_word = 0, None
        for word in words_in_novel:
            if word in ex_word:
                continue
            words_cnt[word] = words_cnt.get(word, 0) +1
            if words_cnt[word] > max_time:
                max_time = words_cnt[word]
                most_frequent_word = word
            elif words_cnt[word] == max_time:
                most_frequent_word = min(word, most_frequent_word, key=lambda s: s.lower())

        return most_frequent_word


if __name__ == '__main__':
    s = Solution()
    text = "fly, eight xx run, ban xx egg, im us ban,"
    ex_words = ["fly","an","a"]
    print(s.frequentWord(text, ex_words))