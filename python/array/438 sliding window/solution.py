from collections import defaultdict

class Solution:
    def findAnagrams(self, p: str, s: str) -> List[int]:
        s = list(s)
        p = list(p)
        start = 0
        end = len(s)
        result = []
        window = defaultdict(int)
        need = defaultdict(int)
        count = 0
        for c in s:
            need[c] += 1
        for d in p[start:start+end]:
            window[d] += 1

        while end <= len(p):
            if window == need:
                result.append(start)
            if end + 1 > len(p):
                break
            window[p[end]] += 1
            window[p[start]] -= 1
            if window[p[start]] <= 0:
                del window[p[start]]
            start += 1
            end += 1
        return result