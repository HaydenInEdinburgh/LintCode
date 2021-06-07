class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.key_to_prev = {}
        self.dummy = Node()
        self.tail = self.dummy

    def get(self, key: int) -> int:
        if key not in self.key_to_prev:
            return -1

        prev = self.key_to_prev[key]
        cur = prev.next
        self.kick(prev)
        return cur.value

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_prev:
            self.kick(self.key_to_prev[key])
            self.key_to_prev[key].next.value = value
            return
        node = Node(key, value)
        self.push_back(node)

        if len(self.key_to_prev) > self.size:
            self.pop_front()

    def kick(self, prev):
        cur = prev.next
        if cur == self.tail:
            return
        prev.next = cur.next
        self.key_to_prev[cur.next.key] = prev
        self.push_back(cur)

    def push_back(self, cur):
        self.tail.next = cur
        self.key_to_prev[cur.key] = self.tail
        self.tail = cur
        cur.next = None

    def pop_front(self):
        head = self.dummy.next
        del self.key_to_prev[head.key]
        self.key_to_prev[head.next.key] = self.dummy
        self.dummy.next = head.next
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)