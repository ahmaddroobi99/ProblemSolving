class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        output = []
        dict = {}

        for i in nums2:
            while stack and stack[-1] < i:
                ele = stack.pop()
                dict[ele] = i
            stack.append(i)

        for i in nums1:
            if i in dict.keys():
                output.append(dict[i])
            else:
                output.append(-1)

        return output