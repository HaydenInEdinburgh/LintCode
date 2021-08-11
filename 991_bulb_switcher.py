import math


class Solution:
    """
    @param n: a Integer
    @return: how many bulbs are on after n rounds
    """
    def bulbSwitch(self, n):
        # Write your code here
        return int(math.sqrt(n))