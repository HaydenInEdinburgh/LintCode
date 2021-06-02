class ListNode:
    def __init__(self, num):
        self.val = num
        self.next = None

class DataStream:

    def __init__(self):
    # do intialization if necessary
        self.dummy = ListNode(0)
        self.tail = self.dummy
        self.num_to_prev = {}
        self.duplicates = set()
    """
    @param num: next number in stream
    @return: nothing
    """

    def add(self, num):
        if num in self.duplicates:
            return

        if num in self.num_to_prev:
            self.duplicates.add(num)
            self.remove(num)
            return

        self.push_back(num)
    # write your code here

    """
    @return: the first unique number in stream
    """

    def firstUnique(self):
    # write your code here
        if not self.dummy.next:
            return None
        return self.dummy.next.val

    def remove(self, num):
        prev = self.num_to_prev[num]
        cur = prev.next

        prev.next = cur.next
        if cur.next:
            self.num_to_prev[cur.next.val] = prev
        else:
            self.tail = prev

    def push_back(self, num):
        self.tail.next = ListNode(num)
        self.num_to_prev[num] = self.tail
        self.tail = self.tail.next