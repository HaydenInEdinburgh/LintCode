import heapq
class Solution:
    """
    @param n: An integer
    @return: return a  integer as description.
    """
    def nthUglyNumber(self, n):
        # write your code here
        if not n:
            return -1

        ugly_numbers= []
        heapq.heappush(ugly_numbers, 1)
        visited = {1}
        cludes = [2, 3, 5]

        cur = 1

        for _ in range(n):
            cur = heapq.heappop(ugly_numbers)
            for c in cludes:
                next = cur * c
                if next not in visited:
                    visited.add(next)
                    heapq.heappush(ugly_numbers, next)

        return cur

if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(9))