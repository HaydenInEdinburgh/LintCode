class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = []

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if len(self.map) < key +1:
            self.map.extend([None]*(key+1-len(self.map)))

        self.map[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if len(self.map) < key+1 or self.map[key] is None:
            return -1

        return self.map[key]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if len(self.map) < key+1:
            return
        self.map[key] = None

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)