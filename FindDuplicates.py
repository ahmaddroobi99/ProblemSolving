class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        arr = []
        for i in range(len(nums)):
            arr.append([nums[i], i])
        arr.sort()
        for i in range(len(arr)-1):
            j = i+1
            while j < len(arr) and abs(arr[i][0] - arr[j][0]) <= t:
                if abs(arr[i][1] - arr[j][1]) <= k:
                    return True
                j += 1
        return False