class Solution:
    """
    @param n:
    @param k:
    @param l: is len
    @param num: //same as problem
    @return: //return long
    """
    def solve(self, n, k, l, num):
        if n < l:
            return 0

        cur_sum = sum(num[:l])
        cnt = 1 if cur_sum/l > k else 0

        for i in range(l, n):
            #print(cur_sum)
            cur_sum = cur_sum + num[i] - num[i-l]
            if cur_sum/l > k:
                cnt += 1

        return cnt

if __name__ == '__main__':
    s = Solution()
    num = [5, 1, 5, 1, 5, 1]
    n = len(num)
    k = 3
    l = 2
    print(s.solve(n, k, l, num))