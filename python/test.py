class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLList:
    def __init__(self):
        self.sentinel = ListNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def delLast(self):
        self.delete(self.sentinel.prev)
        
    def addFront(self, node):
        temp = self.sentinel.next
        self.sentinel.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.sentinel

    def print(self):
        temp = self.sentinel.next
        result = []
        while temp != self.sentinel:
            result.append([temp.key, temp.val])
            temp = temp.next
        print(result)


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = dict()
        self.list = DLList()

    def get(self, key: int) -> int:
        node = self.hashmap[key]
        self.list.delete(node)
        self.list.addFront(node)
        self.list.print()
        return node.val

    def put(self, key: int, value: int) -> None:
        node = ListNode(key, value)
        self.hashmap[key] = node
        self.list.addFront(node)
        self.size += 1
        if self.size > self.capacity:
            self.list.delLast()
            del self.hashmap[key]
            self.size -= 1
        self.list.print()

LRUcache = LRUCache(2)
LRUcache.put(1,1)
LRUcache.put(2,2)
print(LRUcache.get(2))
LRUcache.put(3,3)

