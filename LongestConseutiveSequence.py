class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s, result = set(nums), 0
        for num in nums:
            if (num - 1) in s: continue
            count = 0
            while num + count in s: count += 1
            result = max(result, count)
        return result
class Solution:
        def longestConsecutive(self, nums: List[int]) -> int:
            ans = 0
            # creating a hashset
            s = set(nums)
            for ele in s:
                if ele - 1 in s:
                    continue
                else:
                    k = ele
                    count = 1
                    # checking for the smallest number to start with
                    while (k + 1) in s:
                        count += 1
                        k += 1
                    ans = max(ans, count)
            return ans