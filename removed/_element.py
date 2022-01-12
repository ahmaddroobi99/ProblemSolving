class Solution:
    def removeElement(self, nums, val: int) -> int:
        count = 0
        sizeBeforeRemoving = len(nums)

        for i in range(0,8,1):
            print (nums[i])
            if (nums[i] == val):
                count += 1
                # nums.append(nums[i])
                print (nums[i])
                nums.pop(i)

        return nums

    # len(nums)-count


s=Solution()
print (s.removeElement([0,1,2,2,3,0,4,2],2))