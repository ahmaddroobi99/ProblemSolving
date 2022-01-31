class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key= lambda x: (x[0], -x[1]))
        lis = []

        for w, h in envelopes:
            left = self.binarySearch(lis, h)
            # left is greater than all elements in LIS
            if left == len(lis):
                lis.append(h)
            # Replace the first height that is >= than h with h
            else:
                lis[left] = h

        return len(lis)

    # Return the index within nums that h would be in
    def binarySearch(self, nums, h):
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l) // 2
            if nums[mid] == h:
                return mid
            if nums[mid] < h:
                l = mid + 1
            else:
                r = mid - 1
        return l