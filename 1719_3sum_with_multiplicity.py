import collections
class Solution:
    """
    @param A: the given integer array
    @param target: the given integer target
    @return: the number of tuples
    """

    def threeSumMulti(self, A, target):
        # Write your code here
        n = len(A)
        if n < 3:
            return 0
        num_cnt = collections.Counter(A)

        res = 0
        for i in range(101):
            for j in range(i, 101):
                k = target -i -j
                if k <0 or k >100:
                    continue
                #i==j==k
                cnt = 0
                if i == j == k:
                    cnt = num_cnt[i] * (num_cnt[i] -1) * (num_cnt[i] -2) // 6
                elif i == j != k:
                    cnt = num_cnt[i] * (num_cnt[j] -1) // 2 * num_cnt[k]
                elif j < k:
                    cnt = num_cnt[i] * num_cnt[j] * num_cnt[k]
                res += cnt

        return int(res%(1e9 +7))


if __name__ == '__main__':
    s = Solution()
    A = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    print(s.threeSumMulti(A, target))