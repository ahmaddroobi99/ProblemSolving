class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = [-1]
        for i, num in enumerate(nums):
            if num & 1:
                odd.append(i)
        odd.append(len(nums))

        ans = 0

        for i in range(1, len(odd) - 1):
            if i + k >= len(odd):
                break
            start = odd[i] - odd[i - 1]
            end = odd[i + k] - odd[i + k - 1]
            ans += start * end

        return ans