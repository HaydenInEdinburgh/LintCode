class Solution:
    """
    @param intervals: the intervals
    @param rooms: the sum of rooms
    @param ask: the ask
    @return: true or false of each meeting
    """
    def meetingRoomIII(self, intervals, rooms, ask):
        # Write your code here.
        sum = [0] * 50001
        vis = [0] * 50001
        n = len(ask)
        res = [False] * n

        last = 0
        for start, end in intervals:
            vis[start] += 1
            vis[end] -= 1
            last = max(last, end)

        tmp = 0
        for i in range(n):
            last = max(last, ask[i][1])

        for i in range(1, last+1):
            tmp += vis[i]
            if tmp < rooms:
                sum[i] = 0
            else:
                sum[i] = 1

        for i in range(1, last+1):
            sum[i] += sum[i-1]

        for i in range(n):
            start, end = ask[i]
            if sum[start -1] == sum[end -1]:
                res[i] = True
            else:
                res[i] = False

        return res


if __name__ == '__main__':
    s = Solution()
    intervals = [[1,2],[4,5],[8,10]]
    rooms = 1
    ask = [[2,3],[3,4]]
    print(s.meetingRoomIII(intervals, rooms, ask))