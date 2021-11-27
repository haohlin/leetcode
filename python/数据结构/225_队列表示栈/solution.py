class MyStack:

    def __init__(self):
        self.queue = []
        self.last = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        self.last = x

    def pop(self) -> int:
        size = len(self.queue)
        for i in range(size - 1):
            n = self.queue.pop(0)
            self.queue.append(n)
            self.last = n
        return self.queue.pop(0)        

    def top(self) -> int:
        return self.last

    def empty(self) -> bool:
        if not self.queue:
            return True
        return False