class Solution:
    """
    @param N: a positive number
    @return: how many numbers X from 1 to N are good
    """
    def rotatedDigits(self, N):
        # write your code here
        if not N:
            return None

        res = 0
        for n in range(1, N+1):
            digits = str(n)
            if self.check(digits):
                res += 1

        return res


    def check(self, digits):
        not_valid = {'3', '4', '7'}
        itself = {'1', '0', '8'}
        valid = {'2', '5', '6', '9'}

        flag = False
        for d in digits:
            if d in itself:
                continue
            if d in not_valid:
                return False
            if d in valid:
                flag = True
        return flag

if __name__ == '__main__':
    s = Solution()
    n = 10
    print(s.rotatedDigits(20))