class Solution:
    """
    @param interval_A: a string represent a interval.
    @param interval_B: a string represent a interval.
    @return: if two intervals can merge return true, otherwise false.
    """
    def MergeJudge(self, interval_A, interval_B):
        # write your code here
        if not interval_A or not interval_B:
            return

        first_ch_A, last_ch_A, a_start_bool, a_end_bool = self.process(interval_A)
        first_ch_B, last_ch_B, b_start_bool, b_end_bool = self.process(interval_B)

        if first_ch_A > first_ch_B:
            if last_ch_B > first_ch_A:
                return True
            if (last_ch_B == first_ch_A) and (b_end_bool or a_start_bool):
                return True
            if ((last_ch_B + "a") == first_ch_A) and b_end_bool and a_start_bool:
                return True
            return False
        else:
            if last_ch_A > first_ch_B:
                return True
            if (last_ch_A == first_ch_B) and (a_end_bool or b_start_bool):
                return True
            if ((last_ch_A + "a") == first_ch_B) and a_end_bool and b_start_bool:
                return True
            return False




    def process(self, interval):
        punc_to_bool = {'(': False, ')': False, '[': True, ']': True}
        start_bool, end_bool = punc_to_bool[interval[0]], punc_to_bool[interval[-1]]
        tokens = interval[1:-1].split(',')
        return tokens[0], tokens[-1], start_bool, end_bool

    def processB(self, interval_A):
        first_ch_A = interval_A.split(interval_A[0])[1].split(',')[0]
        last_ch_A = interval_A.split(',')[1].split(interval_A[-1])[0]
        return first_ch_A, last_ch_A

if __name__ == '__main__':
    s = Solution()