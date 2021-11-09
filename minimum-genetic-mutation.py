# import collections
# import queue
# class Solution:
#     def minMutation(self, start: str, end: str, bank: List[str]) -> int:
#         visited = collections.defaultdict(bool)
#         distance = collections.defaultdict(int)
#         bank = set(bank)
#         def bfs():
#             q = queue.Queue()
#             q.put(start)
#             while q.qsize():
#                 top = q.get()
#                 if top == end:
#                     return distance[top]
#                 arr = list(top)
#                 for i in range(8):
#                     letters = {'A', 'C', 'G', 'T'}
#                     for j in letters:
#                         if j != arr[i]:
#                             new_arr = arr[:i] + [j] + arr[i+1:]
#                             new_str = "".join(new_arr)
#                             if new_str in bank and not visited[new_str]:
#                                 visited[new_str] = True
#                                 distance[new_str] = distance[top] + 1
#                                 q.put(new_str)
#             return -1
#         return bfs()


from collections import deque


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:

        if end not in bank:
            return -1

        q = deque()
        q.append((start,0))
        while q:
            tochk,limit = q.popleft()
            if tochk == end:
                return limit

            w = 0
            while w<len(bank):
                word = bank[w]
                c = 0
                for i in range(8):
                    if tochk[i]!=word[i]:
                        c+=1

                if c==1:
                    q.append((word,limit+1))
                    bank.remove(word)
                    continue
                w+=1

        return -1