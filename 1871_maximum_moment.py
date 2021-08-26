class Solution:
    """
    @param time: a string of Time
    @return: The MaximumMoment
    """
    def MaximumMoment(self, time):
        # Write your code here.
        if not time: return None
        res = ''
        if time[0] == '?':
            if time[1] <= '9' and time[1] >= '4':
                res += '1'
            else:
                res += '2'
        else:
            res += time[0]


        if time[1] == '?':
            if res[0] != '2':
                res += '9'
            else:
                res += '3'
        else:
            res += time[1]

        res += ':'

        if time[3] == '?':
            res += '5'
        else:
            res += time[3]

        if time[4] == '?':
            res += '9'
        else:
            res += time[4]

        return res

if __name__ == '__main__':
    s = Solution()
    time = "?2:??"
    print(s.MaximumMoment(time))