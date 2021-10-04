
class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        # write your code here
        if not tasks:
            return 0

        task_cnt = {}

        for t in tasks:
            task_cnt[t] = task_cnt.get(t, 0) + 1

        counts = list(task_cnt.values())
        longest = max(counts)
        res = (longest - 1) * (n + 1) + counts.count(longest)
        return max(res, len(tasks))

if __name__ == '__main__':
    s = Solution()
    tasks = "AAAAAABCDEFG"
    n = 2
    print(s.leastInterval(tasks, n))