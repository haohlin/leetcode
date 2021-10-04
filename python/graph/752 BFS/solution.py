from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        def up_one(num, idx):
            num_list = list(num)
            num_idx = int(num[idx])
            if num_idx != 9:
                num_list[idx] = str(num_idx + 1)
            else:
                num_list[idx] = '0'
            return ''.join(num_list)

        def down_one(num, idx):
            num_list = list(num)
            num_idx = int(num[idx])
            if num_idx != 0:
                num_list[idx] = str(num_idx - 1)
            else:
                num_list[idx] = '9'
            return ''.join(num_list)

        q = ['0000']
        step = 0
        visited = ['0000']
        while q:
            for i in range(len(q)):
                cur = q.pop(0)
                if cur in deadends:
                    continue
                if cur == target:
                    return step
                for i in range(len(cur)):
                    up = up_one(cur, i)
                    down = down_one(cur, i)
                    if up not in visited:
                        visited.append(up)
                        q.append(up)
                    if down not in visited:
                        visited.append(down)
                        q.append(down)
            
            step += 1
        return -1

sol = Solution()
steps = sol.openLock(['8888'], '0009')
print(steps)