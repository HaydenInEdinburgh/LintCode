class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val
        self.data = []

class AllOne:
    """
    @param key: the element given to be added
    @return: nothing
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)
        self.tail = Node(0)
        self.dic = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node, key):
        if node.val+1 != node.next.val: #add another node
            newNode = Node(node.val +1)
            newNode.prev, newNode.next = node, node.next
            newNode.prev.next = newNode.next.prev = newNode
        else:#move the key to next node
            newNode = node.next
        newNode.data.append(key)
        newNode.data.sort(reverse=True)
        return newNode

    def add_prev(self, node, key):
        if node.val -1 != node.prev.val:
            newNode = Node(node.val-1)
            newNode.prev, newNode.next = node.prev, node
            newNode.prev.next = newNode.next.prev = newNode
        else:
            newNode = node.prev
        newNode.data.append(key)
        newNode.data.sort(reverse=True)
        return newNode

    def inc(self, key):
        # write your code here
        if key not in self.dic:
            self.dic[key] = self.add(self.head, key)
        else:
            node = self.dic[key]
            self.dic[key] = self.add(node, key)
            node.data.remove(key)
            if not node.data:
                #remove the node without data
                node.prev.next, node.next.prev = node.next, node.prev
                node.next = node.prev = None
    """
    @param key: pop an element from the queue
    @return: nothing
    """
    def dec(self, key):
        # write your code here
        if key in self.dic:
            node = self.dic[key]
            node.data.remove(key)
            del self.dic[key]
            if node.val > 1:
                self.dic[key] = self.add_prev(node, key)
            if not node.data:
                node.prev.next, node.next.prev = node.next, node.prev
                node.prev = node.next = None
    """
    @return: nothing
    """
    def getMaxKey(self):
        # write your code here
        if not self.tail.prev.data:
            return ""
        num = self.tail.prev.data.pop()
        self.tail.prev.data.append(num)
        return num
    """
    @return: nothing
    """
    def getMinKey(self):
        # write your code here
        if not self.head.next.data:
            return ""
        num = self.head.next.data.pop()
        self.head.next.data.append(num)
        return num

if __name__ == '__main__':
    dic = collections.OrderedDict()
    dic['b'] = 1
    dic['a'] = 2
    dic['c'] = 3
    dic = sorted(dic.items())
    print(dic)