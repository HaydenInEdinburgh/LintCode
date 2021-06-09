class Node:
    def __init__(self, address = None, next = None, prev = None):
        self.address = address
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.dummy = Node()
        home_node = Node(homepage, None, self.dummy)
        self.dummy.next = home_node
        self.current = home_node
        self.tail = home_node
        print(self.current.address)
    def visit(self, url: str) -> None:
        new_visit_node = Node(url, None, self.current)
        self.current.next = new_visit_node

        self.tail = new_visit_node
        self.current = new_visit_node
        print(self.current.address)
    def back(self, steps: int) -> str:
        for _ in range(steps):
            #print(self.current.address)
            if self.current == self.dummy.next:
                #print('back break')
                break
            self.current = self.current.prev

        print(self.current.address)
        return self.current.address

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.current == self.tail:
                break
            self.current = self.current.next

        print(self.current.address)
        return self.current.address

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
if __name__ == '__main__':
    b = BrowserHistory('leetcode.com')
    b.visit('google.com')
    b.back(7)
    b.forward(1)
    b.visit('linkedin.com')
    b.forward(2)
    b.back(2)
    b.back(7)