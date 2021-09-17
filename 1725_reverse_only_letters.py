class Solution:
    """
    @param S: Customary string
    @return: Reversed string
    """
    def ReverseOnlyLetters(self, S):
        # write your code here
        if not S:
            return ''

        n = len(S)
        letters = list(S)
        l, r = 0, n-1

        while l < r:
            while l <r and not letters[l].isalpha():
                l += 1
            while l <r and not letters[r].isalpha():
                r -= 1
            if l <r:
                letters[l], letters[r] = letters[r], letters[l]
                l += 1
                r -= 1

        return ''.join(letters)
