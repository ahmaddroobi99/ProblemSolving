
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = 0
        dict_output = {}
        for i in nums1:
            for j in nums2:
                if i+j in dict_output.keys():
                    dict_output[i+j] += 1
                else:
                    dict_output[i+j] = 1
        for i in nums3:
            for j in nums4:
                if -(i+j) in dict_output.keys():
                    counter += dict_output[-(i+j)]
        return counter