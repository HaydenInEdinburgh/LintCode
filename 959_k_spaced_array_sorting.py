import heapq


class Solution:
    """
    @param arr: The K spaced array
    @param k: The param k
    @return: Return the sorted array
    """
    def getSortedArray(self, arr, k):
        # Write your code here
        n = len(arr)

        stack = []
        for i in range(k):
            heapq.heappush(stack, (arr[i], i))

        res = []
        while stack:
            a, idx = heapq.heappop(stack)
            res.append(a)
            if idx+k < len(arr):
                heapq.heappush(stack, (arr[idx+k], idx+k))

        return res

if __name__ == '__main__':
    s = Solution()
    arr = [4,0,5,3,10]
    k = 2
    print(s.getSortedArray(arr, k))