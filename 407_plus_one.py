class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        if not digits: return

        res = []
        p = 0
        for i in range(len(digits)-1, -1, -1):
            n = digits[i]+1 if i == len(digits)-1 else digits[i]
            d_i = (n + p) %10
            p = (n + p) //10
            print(n+p)
            res.append(d_i)

        if p != 0:
            res.append(p)

        return res[::-1]

if __name__ == '__main__':
    s = Solution()
    digits = [1, 9, 9, 9]
    print(s.plusOne(digits))
