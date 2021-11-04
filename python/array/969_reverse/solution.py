from typing import List

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        for i in reversed(range(1, len(arr))):
            max_i = 0
            max_n = 0
            for j,n in enumerate(arr[:i+1]):
                if n > max_n:
                    max_n = n
                    max_i = j
            if max_i == i:
                continue
            self.reverse(arr, max_i)
            self.reverse(arr, i)
            result.append(max_i+1)
            result.append(i+1)
        return result

    def reverse(self, arr, end):
        i = 0
        j = end
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
