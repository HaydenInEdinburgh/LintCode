class Solution:
    """
    @param arr: an integer array
    @return: return the median array when delete a number
    """
    def getMedian(self, arr):
        # write your code here
        n = len(arr)
        if n <= 1:
            return []

        arr_sorted = sorted([[val, index] for index, val in enumerate(arr)])
        res = []
        m_idx_1 = n//2 - 1
        m_1 = arr_sorted[m_idx_1][0]
        m_idx_2 = n//2
        m_2 = arr_sorted[m_idx_2][0]

        for i in range(n):
            if i < m_idx_2:
                arr_sorted[i] = [arr_sorted[i][1], m_2]
            else:
                arr_sorted[i] = [arr_sorted[i][1], m_1]

        return [val for index, val in sorted(arr_sorted)]

if __name__ == '__main__':
    s = Solution()
    arr = [5, 2, 4, 3, 1]
    print(s.getMedian(arr))