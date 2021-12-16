class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        ans = []
        for _ in range(n):
            diff = sums[1] - sums[0]
            ss0, ss1 = [], []
            freq = defaultdict(int)
            on = False
            for i, x in enumerate(sums):
                if not freq[x]:
                    ss0.append(x)
                    freq[x+diff] += 1
                    if x == 0: on = True
                else: 
                    ss1.append(x)
                    freq[x] -= 1
            if on:
                ans.append(diff)
                sums = ss0
            else:
                ans.append(-diff)
                sums = ss1
        return ans