class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(arr)
        odd_sum, even_sum, curr_sum, ans = 0, 1, 0, 0
        for i in arr:
            curr_sum += i
            if curr_sum % 2 == 1:
                odd_sum += 1
                ans += even_sum % mod
            else:
                even_sum += 1
                ans += odd_sum % mod
        ans %= mod
        return ans
    