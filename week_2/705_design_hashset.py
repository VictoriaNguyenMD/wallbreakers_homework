class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = []
        

    def add(self, key: int) -> None:
        if self.contains(key) == False:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.set.remove(key)
        
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        for num in self.set:
            if num == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
