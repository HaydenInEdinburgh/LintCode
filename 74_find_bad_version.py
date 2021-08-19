class SVNRepo:
   @classmethod
   def isBadVersion(cls, id):
       # Run unit tests to check whether verison `id` is a bad version
       # return true if unit tests passed else false.
        return
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        # write your code here
        if not n:
            return None
        if n <= 1:
            return 1
        checker = SVNRepo()
        l, r = 0, n
        while l+1< r:
            mid = (l+r)//2
            if checker.isBadVersion(mid):
                r = mid
            else:
                l = mid
        if checker.isBadVersion(l):
            return l
        if checker.isBadVersion(r):
            return r
        return -1