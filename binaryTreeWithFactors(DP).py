class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        dp = [1] * n

        arrSet = set(arr)
        numIndex = {num: i for i, num in enumerate(arr)}
        for i in range(1, n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    num2 = arr[i] // arr[j]
                    if num2 in arrSet:
                        index2 = numIndex[num2]
                        dp[i] += dp[j] * dp[index2]

        mod = 10 ** 9 + 7
        return sum(dp) % mod
