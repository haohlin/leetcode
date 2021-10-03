# find the shortest distance from start to target

class Solution:
    def BFS(self, start, target):
        q = []
        q.append(start[0])
        step = 0
        visited = [q[0]]
        while q:
            step += 1
            for i in range(len(q)):
                if q[0].val == target:
                    return step
                first = q.pop(0)
                for child in q.child:
                    if q[0] not in visited:
                        visited.append(q[0])
                    else:
                        continue
                    q.append(child)
        return -1

