class Solution:
    """
    @param A:
    @return: nothing
    """
    def playGames(self, A):
        # Write your code here
        low = max(A)
        high = sum(A)

        while low+1 <high:
            mid = (low +high)//2
            if self.is_enough(mid, A):
                high = mid
            else:
                low = mid

        if self.is_enough(low, A):
            return low
        else:
            return high

    def is_enough(self, num, A):
        num_play_judge = 0
        for a in A:
            num_play_judge += (num -a)

        return num_play_judge >= num

