import heapq
from typing import List


class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = [0] * len(tasks)
        available = [(servers[i], i) for i in range(len(servers))]
        avaliable = heapq.heapify(available)
        unavail = []

        t = 0
        for i in range(len(tasks)):
            t = max(t, i)

            if len(available) == 0:
                t = unavail[0][0]
            while unavail and t >= unavail[0][0]:
                timefree, wight, index = heapq.heappop(unavail)
                heapq.heappush(available, (wight, index))
            wight, index = heapq.heappop(available)
            res[i] = index
            heapq.heappush(unavail, (t + tasks[i], wight, index))
        return res





