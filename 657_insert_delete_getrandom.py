import random
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class RandomizedSet:

    def __init__(self):

    # do intialization if necessary
        self.value_to_index = {}
        self.dummy = Node(-sys.maxsize)
        self.value_to_index[self.dummy.value] = -1
        self.tail = self.dummy
        self.size = 0
    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """

    def insert(self, val):

    # write your code here
        if val in self.value_to_index:
            return False
        node = Node(val)
        self.size += 1
        self.value_to_index[node.value] = self.value_to_index[self.tail.value] + 1
        self.tail.next = node
        self.tail = node

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """

    def remove(self, val):

    # write your code here
        if val not in self.value_to_index:
            return False
        inx = self.value_to_index[val]
        # find prev node
        prev = self.dummy
        for _ in range(inx):
            prev = prev.next

        node = prev.next
        if self.tail == node:
            self.tail = prev
        prev.next = node.next
        del self.value_to_index[node.value]

        node = node.next
        while node:
            self.value_to_index[node.value] -= 1
            node = node.next

        self.size -= 1

        return True

    """
    @return: Get a random element from the set
    """

    def getRandom(self):
        if not self.size:
            return False
        index = random.randint(0, self.size-1)
        node = self.dummy
        for _ in range(index +1):
            node = node.next

        return node.value
# write your code here


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()

if __name__ == '__main__':
    s = RandomizedSet()
    s.insert(1)
    print(s.remove(2))
    s.insert(2)
    print(s.getRandom())
    print(s.value_to_index)