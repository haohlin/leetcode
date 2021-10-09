class Deque:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.sentinal = Deque()
        self.sentinal.next = self.sentinal
        self.sentinal.prev = self.sentinal
        self.hash_map = dict()


    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.move_to_front(self.hash_map[key])
            return self.hash_map[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.move_to_front(node)
        else:
            new_node = Deque(key, value)
            self.add_front(new_node)
            self.hash_map[key] = new_node
            if self.size > self.capacity:
                self.remove_last()

    
    def move_to_front(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        self.add_front(node)

    def add_front(self, node):
        self.size += 1
        self.sentinal.next.prev = node
        node.prev = self.sentinal
        node.next = self.sentinal.next
        self.sentinal.next = node
    
    def remove_last(self):
        self.size -= 1
        node = self.sentinal.prev
        self.hash_map.pop(node.key)
        node.prev.next = self.sentinal
        self.sentinal.prev = node.prev

lRUCache =  LRUCache(2)
lRUCache.put(1, 1)# 缓存是 {1=1}
lRUCache.put(2, 2)# 缓存是 {1=1, 2=2}
lRUCache.get(1)# 返回 1
lRUCache.put(3, 3)# 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2)# 返回 -1 (未找到)
lRUCache.put(4, 4)# 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1)# 返回 -1 (未找到)
lRUCache.get(3)# 返回 3
lRUCache.get(4)# 返回 4
