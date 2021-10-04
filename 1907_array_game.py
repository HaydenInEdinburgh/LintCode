from typing import (
    List,
)

class Solution:
    """
    @param arr: the array
    @return: determine the number of moves to make all elements equals
    """
    def arrayGame(self, arr: List[int]) -> int:
        # write your code here
        if not arr:
            return 0
        minimum = min(arr)

        step = 0
        for n in arr:
            step += (n-minimum)

        return step

if __name__ == '__main__':
    s = Solution()
    arr = [3, 4, 6, 6, 3]
    print(s.arrayGame(arr))