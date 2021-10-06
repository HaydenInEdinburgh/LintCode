class Solution:
    """
    @param s: a string
    @return: reverse only the vowels of a string
    """
    def reverseVowels(self, s):
        # write your code here
        if not s:
            return s
        s = list(s)
        vowels = "aeiouAEIOU"
        n = len(s)
        #get the first v's index
        l = 0
        while l <n:
            if s[l] in vowels:
                break
            l += 1

        if l >= n:
            return s

        r = n-1
        while r >=0:
            if s[r] in vowels:
                break
            r -= 1
        #print(l, r)
        while l< r:
            s[l], s[r] = s[r], s[l]
            #print(s)
            l +=1
            r -=1
            while l<r and s[l] not in vowels:
                l += 1
            while l<r and s[r] not in vowels:
                r -= 1

        return ''.join(s)

if __name__ == '__main__':
    s = Solution()
    string = 'hello'
    print(s.reverseVowels(string))