from typing import List

class Solution1:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        p_1 = self.power(a, last)
        p_2 = self.power(self.superPow(a,b), 10)
        return (p_1 * p_2) % 1337

    def power(self, a, p):
        a %= 1337
        res = 1
        for i in range(p):
            res *= a
            res %= 1337
        return res

class Solution2:
    def superPow(self, a: int, b: List[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        p_1 = self.power(a, last)
        p_2 = self.power(self.superPow(a,b), 10)
        return (p_1 * p_2) % 1337

    def power(self, a, p): # Faster Power
        if p == 0:
            return 1
        a %= 1337
        if p % 2 == 0:
            p1 = self.power(a, p / 2)
            return (p1 * p1) % 1337
        else:
            return (self.power(a, p - 1) * a) % 1337