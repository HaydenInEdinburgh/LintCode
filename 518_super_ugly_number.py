import heapq


class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        # write your code here
        if not n or not primes:
            return None
        if n == 1: return 1
        visited = set(primes)
        min_heap = sorted(primes)

        for _ in range(n-1):
            number = heapq.heappop(min_heap)
            print(number)
            for p in primes:
                if p * number in visited:
                    continue
                heapq.heappush(min_heap, p* number)
                visited.add(p*number)

        return number

if __name__ == '__main__':
    s = Solution()
    n = 7
    primes = [149,197,113,163,2,61,83]
    print(s.nthSuperUglyNumber(n, primes))

