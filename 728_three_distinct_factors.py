import math


class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """
    def isThreeDisctFactors(self, n):
        # write your code here
        sq = int(math.sqrt(n))
        if (sq * sq != n):
            return False
        return self.isPrime(n)

    def isPrime(self, n):
        if n <= 1: return False
        if n <= 3: return True
        if (n %2 == 0 or n %3 == 0): return False
        i = 5
        while (i * i <=n):
            if (n %i == 0 or n%(i+2) ==0):
                return False
            i += 6

        return True


if __name__ == '__main__':
    s = Solution()
    n = 10
    print(s.isThreeDisctFactors(n))