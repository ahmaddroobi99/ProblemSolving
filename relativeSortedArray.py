class Solution:
    def relativeSortArray(self, arr1, arr2):
        dict = {}
        nums, ans = [], []

        for val in arr2:
            dict[val] = 0

        for val in arr1:
            if val not in dict:
                nums.append(val)
            else:
                dict[val] += 1

        for key, val in dict.items():
            ans.extend([key for _ in range(val)])

        ans.extend(sorted(nums))
        return ans
