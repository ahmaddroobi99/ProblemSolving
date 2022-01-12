class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort() # O(nlogn)
        return nums[len(nums) -k]