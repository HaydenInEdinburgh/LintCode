class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    def findNthDigit(self, n):
        # write your code here
        if not n:
            return None

        length, count, start = 1, 9, 1
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10
        #find the exact number
        start += (n-1) // length
        return int(str(start)[(n-1)%length])

if __name__ == '__main__':
    s = Solution()
    print(s.findNthDigit(11))