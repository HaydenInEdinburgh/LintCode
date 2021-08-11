import sys


class Solution:
    """
    @param v1: the speed of GGbond
    @param v2: the speed of SuperQ
    @param s: the speed that lollipop can add
    @param w: the cost of lollipop
    @return: the minimal price
    """
    def getAns(self, v1, v2, s, w):
        # Write your code here
        if not s or not w:
            return
        if v1 > v2:
            return 0
        price = sys.maxsize
        for i, speed_add in enumerate(s):
            p = w[i]
            if v1 + speed_add > v2:
                price = min(price, p)

        return price