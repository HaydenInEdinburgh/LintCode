import heapq
class Solution:
    """
    @param arr: An array
    @return: Get the three largest numbers in the array
    """
    def TopThree(self, arr):
        # write your code here
        if not arr:
            return []

        top_stack = []
        visited = set()
        for i in range(len(arr)):
            num = arr[i]
            if num in visited:
                continue
            if len(top_stack) < 3:#not enough
                heapq.heappush(top_stack, num)
                visited.add(num)
            else:
                if num > top_stack[0]:
                    smallest = heapq.heappop(top_stack)
                    print(smallest)
                    heapq.heappush(top_stack, num)
                    visited.remove(smallest)
                    visited.add(num)

        return sorted(top_stack, reverse=True)

if __name__ == '__main__':
    s = Solution()
    arr = [997, 996, 997, 1001, 1000,1000,1000,999,998, ]
    print(s.TopThree(arr))