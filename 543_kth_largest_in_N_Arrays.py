import heapq


class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        # write your code here
        if not arrays:
            return
        sorted_arrs = []
        for arr in arrays:
            if not arr:
                continue
            sorted_arrs.append(sorted(arr, reverse=True))

        heap = []
        # append the head of arrs
        for i in range(len(sorted_arrs)):
            heapq.heappush(heap, (-sorted_arrs[i][0], i, 0))

        for _ in range(k):
            num, x, y = heapq.heappop(heap)
            if y+1 < len(sorted_arrs[x]):
                heapq.heappush(heap, ( -sorted_arrs[x][y+1], x, y+1))

        return - num
