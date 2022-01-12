class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = []  # To store results
        l1 = {}  # to store item and it's index
        for i, item in enumerate(list1):
            l1[item] = i

        min_ind = 2 ** 32  # default least index
        for i, item in enumerate(list2):
            if item in l1:  # check if item from list2 exist in list1
                ind = i + l1[item]
                if ind == min_ind:  # check if current index is same as min_ind
                    result.append(item)
                elif ind < min_ind:  # got new least index so replace result and also change min_ind
                    result = [item]
                    min_ind = ind

        return result