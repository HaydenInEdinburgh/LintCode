class Solution:
    """
    @param num: An integer
    @return: true if num is an ugly number or false
    """

    def isUgly(self, num):
        # write your code here
        if not num:
            return False
        if num == 1:
            return True

        cludes = {2, 3, 5}
        for c in cludes:
            if num % c == 0:
                if num / c == 1:
                    return True
                else:
                    return self.isUgly(num / c)

        return False

if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(14))
