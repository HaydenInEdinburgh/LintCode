import heapq
class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def removeDuplicateLetters(self, s):
        # write your code here
        if not s:
            return ''

        char_cnt = {}
        for char in s:
            char_cnt[char] = char_cnt.get(char, 0) + 1

        stack = []
        used = set()
        for char in s:
            char_cnt[char] -= 1
            if char in used:
                continue
            while stack and ord(char) < ord(stack[-1]) and char_cnt[stack[-1]] >0:
                used.remove(stack.pop())
            stack.append(char)
            used.add(char)

        return ''.join(stack)
