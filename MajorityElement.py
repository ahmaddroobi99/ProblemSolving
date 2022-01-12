class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        my_dic = {}
        for i in nums:
            if i in my_dic:
                my_dic[i] += 1
            else:
                my_dic[i] = 1

        maximum = max(my_dic.values())
        for i, j in my_dic.items():
            if j == maximum:
                return i
