class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = [0] * 201  # -100 <= nums[i] <= 100
        for n in nums:
            counts[n + 100] += 1

        freqs = [[] for _ in range(101)]  # 1 <= nums.length <= 100
        for n in range(200, -1, -1):
            if counts[n]:
                freqs[counts[n]].append(n - 100)

        result = []
        for freq, arr in enumerate(freqs):
            for n in arr:
                result.extend([n] * freq)