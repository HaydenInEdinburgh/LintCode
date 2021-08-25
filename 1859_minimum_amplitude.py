import sys


class Solution:
    """
    @param A: a list of integer
    @return: Return the smallest amplitude
    """
    def MinimumAmplitude(self, A):
        # write your code here
        if not A:
            return

        A.sort()
        amp = sys.maxsize
        for i in range(4):
            j = len(A)-1-(3-i)
            if i <= j:
                amp = min(A[j]-A[i], amp)
            else:
                amp = 0
        return amp

if __name__ == '__main__':
    s = Solution()
    A = [-4,20,-16,-48,-47,50,-18,-27,-14,-45,-33,-32,-19,-40,1,40,43,-29,16,-43,19,-49,36,-37,-14,-2,46,-19,45,-14,-26,8,-34,42,2,43,-18,-41,36,-7,38,37,43,-43,21,23,14,-19,12,10,5,-31,-20,-10,-18,44,45,0,9,-4,39,39,40,-39,48,-47,-20,-26,50,7,31,36,-18,29,24,30,-8,16,-39,-33,-41,-9,18,-9,30,19,-14,-16,3,-35,-10,31,-2,17,39,14,-17,42,-27,13]
    print(s.MinimumAmplitude(A))