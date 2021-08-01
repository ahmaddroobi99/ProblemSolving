class Solution:
    def majorityElement(self, nums) -> int:
        temp = {}

        for i in nums:
            temp[i] +=1
        max_element = temp[0].value
        max_element_index = 0
        for key, value in temp:
            if temp[key].value > max_element:
                max_element = temp[key].value
                max_element_index = key

            else:
                continue

        return max_element_index



s= Solution ()
print(s.majorityElement([2,2,1,1,1,1,5]))



