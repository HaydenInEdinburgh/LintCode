class Node:
    def __init__(self, val=None, next=None):
        self.value = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dummy = Node()
        self.tail = self.dummy
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index + 1 > self.size:
            return -1

        node = self.dummy
        for _ in range(index+1):
            node = node.next
        return node.value

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.size == 0:
            self.dummy.next = node
            self.tail = node
        else:
            old_head = self.dummy.next
            self.dummy.next = node
            node.next = old_head

        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:
            return

        if index == self.size:
            self.addAtTail(val)
            return
        node = Node(val)
        # find the prev node
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        old_node_at_index = prev.next
        prev.next = node
        node.next = old_node_at_index

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:
            return

        # find the prev node
        prev = self.dummy
        for _ in range(index):
            prev = prev.next

        old_node_at_index = prev.next
        old_next = old_node_at_index.next
        prev.next = old_next

        if index + 1 == self.size: # delete the tail
            self.tail = prev

        self.size -= 1

