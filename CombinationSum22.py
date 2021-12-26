class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result: List[int] = []

        def dfs(current: List[int], start: int, currentSum: int):
            if currentSum == target:
                result.append([] + current)
                return

            lookup = {}
            for i in range(start, len(candidates)):
                num = candidates[i]
                if num + currentSum > target:
                    break
                if num in lookup:
                    continue
                current.append(num)
                dfs(current, i + 1, currentSum + num)
                current.pop()
                lookup[num] = True

        dfs([], 0, 0)
        return result