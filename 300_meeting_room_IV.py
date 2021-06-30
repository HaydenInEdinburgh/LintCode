class meeting:
    def __init__(self, start, end, value):
        self.start = start
        self.end = end
        self.value = value

class Solution:
    """
    @param meeting: the meetings
    @param value: the value
    @return: calculate the max value
    """
    def maxValue(self, meetings, value):
        # write your code here
        if not meetings:
            return 0
        n = len(meetings)
        meeting_list = [meeting(meetings[i][0], meetings[i][1], value[i]) for i in range(n)]
        meeting_list.sort(key= lambda m: m.end)
        dp = [0] * n

        for i in range(n):
            if i == 0:
                dp[i] = meeting_list[i].value
                continue
            cur_val = meeting_list[i].value
            idx = self.binary_search(meeting_list, i-1, meeting_list[i].start)
            print(idx)
            if idx == -1:
                # no valid prev meeting
                dp[i] = max(cur_val, dp[i-1])
            else:
                dp[i] = max(dp[idx] + cur_val, dp[i-1])

        return dp[n-1]

    def binary_search(self, meeting_list, right, target):
        # find the last meeting whose end time is not larger than target
        left = 0
        while left +1< right:
            mid = (left + right) //2
            if meeting_list[mid].end <= target:
                left = mid
            else:
                right = mid

        if meeting_list[right].end <= target: return right
        if meeting_list[left].end <= target: return left
        return -1

if __name__ == '__main__':
    meetings = [[10, 40], [30, 45], [20, 50], [40, 60]]
    value = [3, 6, 2, 4]
    s = Solution()
    print(s.maxValue(meetings, value))