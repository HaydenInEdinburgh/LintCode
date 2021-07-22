class Solution:
    """
    @param str: the pattern
    @return: the minimum number
    """
    def formMinimumNumber(self, string):
        # Write your code here.
        if not string:
            return ""

        string = 'I' + string
        digits = [str(d) for d in range(9, 0, -1)]
        res = ''
        left, right = 0, 1
        while len(res) < len(string):
            if right < len(string) and string[right] != 'I':
                right += 1
                continue
            #find next I
            tmp = ''
            for _ in range(right-left):
                char = digits.pop()
                tmp += char
            res += tmp[::-1]
            left = right
            right += 1

        return res

if __name__ == '__main__':
    s = Solution()
    string = 'II'
    print(s.formMinimumNumber(string))