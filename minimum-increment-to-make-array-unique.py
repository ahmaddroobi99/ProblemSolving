class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        seen = set()
        ans =0
        nums.sort()
        prev = nums[0]
        for n in nums:
            if n not in seen:
                seen.add(n)
                prev= n
            else:
                seen.add(prev+1)
                ans += prev - n +1
                prev+=1
        return ans