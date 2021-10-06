from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0] * (n + 1)
        result = [0] * (n + 1)
        
        for l in bookings:
            diff[l[0]] += l[2]
            if l[1] == n:
                continue
            else:
                diff[l[1]+1] -= l[2]
        
        for i in range(1, len(result)):
            result[i] = result[i - 1] + diff[i]
        return result[1:]