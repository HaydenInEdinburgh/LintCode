import sys


class Solution:
    """
    @param father: the father of every node
    @param time: the time from father[i] to node i
    @return: time to flower tree
    """
    def timeToFlowerTree(self, father, time):
        # write your code here
        n = len(father)
        if n < 2:
            return 0
        memo = {}
        res = 0
        for i in range(1, len(father)):
            time_spent = self.dfs(father, time, i, memo)
            res = max(res, time_spent)
        return res

    def dfs(self, father, time, root, memo):
        if root == 0:
            return 0

        if root in memo:
            return memo[root]

        memo[root] = time[root] + self.dfs(father, time, father[root], memo)

        return memo[root]
if __name__ == '__main__':
    s = Solution()
    father = [-1,2,0]
    time = [-1,3,5]
    print(s.timeToFlowerTree(father, time))