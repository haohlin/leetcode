from typing import List

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        digit_pat = self.patternToDigit(pattern)
        result = []
        for word in words:
            if self.patternToDigit(word) == digit_pat:
                result.append(word)
        return result 

    def patternToDigit(self, s):
        ptr = 0
        record = dict()
        digit_pattern = []
        for c in s:
            if c in record:
                pass
            else:
                ptr += 1
                record[c] = ptr
            digit_pattern.append(record[c])
        return digit_pattern

