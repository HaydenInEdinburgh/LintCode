class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def isPossible(self, nums):
        # write your code here
        freq = {}
        tail = {}
        for n in nums:
            freq[n] = freq.get(n, 0) +1
            tail[n] = 0

        for n in nums:
            if not freq[n]:
                continue

            if n-1 in tail and tail[n-1] >0:
                tail[n-1] -=1
                tail[n] += 1

            elif n+1 in freq and n+2 in freq and freq[n+1] >0 and freq[n+2] >0:
                freq[n+1] -=1
                freq[n+2] -=1
                tail[n+2] += 1
            else:
                return False

            freq[n] -=1

        return True
