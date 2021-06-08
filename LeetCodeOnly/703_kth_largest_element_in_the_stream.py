import heapq


class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.numbers = nums
        heapq.heapify(self.numbers)
        while len(self.numbers) > k:
            heapq.heappop(self.numbers)

    def add(self, val: int) -> int:
        if len(self.numbers) < self.k:
            heapq.heappush(self.numbers, val)
        elif val > self.numbers[0]:
            heapq.heapreplace(self.numbers, val)
        print(self.numbers)
        return self.numbers[0]
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

if __name__ == '__main__':
    k = 3
    nums = [4, 5, 8, 2]
    s = KthLargest(k, nums)
    s.add(3)
    s.add(5)
    s.add(5)
