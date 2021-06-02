class ListNode:
    def __init__(self, num):
        self.val = num
        self.next = None

class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """
    def __init__(self):
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.duplicates = set()
        self.num_to_prev = {}

    def firstUniqueNumber(self, nums, number):
        # Write your code here
        if not nums or not number:
            return None

        for n in nums:
            if n in self.duplicates:
                continue
            if n in self.num_to_prev:
                self.remove(n)
                self.duplicates.add(n)
                continue
            self.push_back(n)
            if n == number:
                # print(self.duplicates)
                return self.dummy.next.val

        return -1

    def remove(self, n):
        # print('remove', n)
        prev = self.num_to_prev[n]
        cur = prev.next
        prev.next = cur.next
        if cur.next:
            self.num_to_prev[cur.next.val] = prev
        else:
            self.tail = prev
        # if self.dummy.next:
        #     print('dead is:', self.dummy.next.val)
        # else:
        #     print('Nothing')
    def push_back(self, n):
        # print('pushback', n)
        self.tail.next = ListNode(n)
        self.num_to_prev[n] = self.tail
        self.tail = self.tail.next
        # if self.dummy.next:
        #     print('dead is:', self.dummy.next.val)
        # else:
        #     print('Nothing')
if __name__ == '__main__':
    s = Solution()
    nums = [1, 2, 2, 1, 3, 4, 4, 5, 6]
    number = 5
    print(s.firstUniqueNumber(nums, number))