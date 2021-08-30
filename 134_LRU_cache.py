class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # do intialization if necessary
        self.dummy = Node()
        self.capacity = capacity
        self.key_to_prev = {}
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
        curr = prev.next
        self.kick(prev)

        return curr.value

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """

    def set(self, key, value):
        # write your code here
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value  # update value
            return
        self.push_back(Node(key, value))
        if self.capacity < len(self.key_to_prev):
            self.pop_front()

    def kick(self, prev):  # move a node to the tail
        node = prev.next 
        if node == self.tail:  # has been tail
            return
        prev.next = node.next  #
        self.key_to_prev[node.next.key] = prev
        node.next = None
        self.push_back(node)

    def push_back(self, node):
        self.key_to_prev[node.key] = self.tail
        self.tail.next = node
        self.tail = node

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.dummy.next = head.next
        self.key_to_prev[head.next.key] = self.dummy
