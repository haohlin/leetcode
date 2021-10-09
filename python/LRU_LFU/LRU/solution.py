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
        pass

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            node.value = value
            self.move_to_front(node)
        else:
            new_node = Deque(key, value)
            self.add_front(new_node)
    
    def move_to_front(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.add_front(node)

    def add_front(self, node):
        self.sentinal.next.prev = node
        node.prev = self.sentinal
        node.next = self.sentinal.next
        self.sentinal.next = node