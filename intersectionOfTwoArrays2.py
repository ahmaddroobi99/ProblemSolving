class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i = j = 0
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i] < nums2[j]:
                i = i + 1
            elif nums1[i] == nums2[j]:
                n.append(nums1[i])
                i = i + 1
                j = j + 1
            elif nums1[i] > nums2[j]:
                j = j + 1
        return n