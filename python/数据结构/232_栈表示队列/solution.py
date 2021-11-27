class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        self.s2.append(x)


    def pop(self) -> int:
        if not self.s1:
            while self.s2:
                n = self.s2.pop()
                self.s1.append(n)
        return self.s1.pop()

    def peek(self) -> int:
        if not self.s1:
            while self.s2:
                n = self.s2.pop()
                self.s1.append(n)
        return self.s1[-1]

    def empty(self) -> bool:
        if not self.s1 and not self.s2:
            return True
        return False