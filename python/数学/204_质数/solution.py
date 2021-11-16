import math

class Solution1: # Slow
    def countPrimes(self, n: int) -> int:
        result = []
        for i in range(2, n):
            isPrime = True
            for res_i in result:
                if res_i * res_i > i:
                    break
                if i % res_i == 0:
                    isPrime = False
                    break
            if isPrime:
                result.append(i)
        return len(result)

class Solution2: # Faster
    def countPrimes(self, n: int) -> int:
        isPrime = [1 for i in range(n)]
        if not isPrime:
            return 0
        for i in range(2, int(math.sqrt(n - 1)) + 1):
            if isPrime[i] == 1:
                for j in range(i, n):
                    if i * j > n - 1:
                        break
                    isPrime[i*j] = 0
        return sum(isPrime[2:])