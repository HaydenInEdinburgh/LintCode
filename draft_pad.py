class Node(object):
    """docstring for Node"""

    def __init__(self, key=None, val=None, next=None):
        self.val = val
        self.key = key
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.key_to_prev = {}
        self.dummy = Node()
        self.tail = self.dummy

    """
    @param: key: An integer
    @return: An integer
    """

    def get(self, key):
        # write your code here
        if key not in self.key_to_prev:
            return -1
        prev = self.key_to_prev[key]
        print(prev.val)
        curr = prev.next
        self.kick(prev)

        return curr.val

    """
    @param: key: An integer
    @param: val: An integer
    @return: nothing
    """

    def set(self, key, val):
        # write your code here
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.val = val  # update val
            print(key, self.key_to_prev[key].next.val, val)
            return
        self.push_to_tail(Node(key, val))
        if self.capacity < len(self.key_to_prev):
            self.pop_front()

    def kick(self, prev):
        curr = prev.next
        if curr == self.tail:
            return

        prev.next = curr.next
        self.key_to_prev[curr.next.key] = prev
        curr.next = None
        self.push_to_tail(curr)

    def push_to_tail(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy

if __name__ == '__main__':
    L = LRUCache(2)
    L.set(2, 2)
    L.set(2, 1)
    print(L.get(2))