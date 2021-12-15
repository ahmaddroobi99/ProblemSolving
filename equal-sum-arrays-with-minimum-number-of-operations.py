class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # idea is to decrement values the array having larger sum and increment values in the array having small sum
        # choose biggest element always to decrement values in large_sum_array
        # choose smallest element always to increment values in small_sum_array
        # both above points suggest , to have sorted arrays for better selection
        # Now , once you get to this point , we need to select whether to decrement or increment in either of array for that
        # we need to check which one in either of them , making differnece smaller and select that

        sum1 = sum(nums1)
        sum2 = sum(nums2)

        if sum1 == sum2:  # if sum is same , nothing is needed
            return 0
        # sort arrays , that will help in selecting elements in sorted order
        nums1.sort()
        nums2.sort()

        # below is needed to make the code is simple
        if sum1 > sum2:
            larger_sum_array, smaller_sum_array = nums1, nums2
        else:
            larger_sum_array, smaller_sum_array = nums2, nums1

        # normal initialization
        largeSum = sum(larger_sum_array)
        smallSum = sum(smaller_sum_array)
        largeSumArrayLen = len(larger_sum_array)
        smallSumArrayLen = len(smaller_sum_array)

        left, right = 0, largeSumArrayLen - 1
        count = 0
        diff = largeSum - smallSum

        # we will have 2 pointer , right will iterate over large_sum_array for decreasing, biggest element
        # left will iterate over small_sum_array for incrementing, smallest element
        # once you see, which way is better minimizing diff of 2 arrays , move pointers accordingly

        while left < smallSumArrayLen and right >= 0:

            diffIfDecrement = diff - (
                        larger_sum_array[right] - 1)  # value if you decide on decrement in largest sum array
            diffIfIncrement = diff - (
                        6 - smaller_sum_array[left])  # value if you decide on increment in small_sum_array

            if diffIfIncrement < diffIfDecrement:  # selection which way is better i.e. who minimizes the diff better
                smallSum += (6 - smaller_sum_array[left])
                left += 1
            else:
                largeSum -= (larger_sum_array[right] - 1)
                right -= 1
            count += 1

            diff = largeSum - smallSum
            if diff <= 0:  # point where largeSum is going down => suggests that point where sum can be equal
                return count

        while left < smallSumArrayLen:  # largest_sum_array exhausted , only way is increment in small_sum_array
            smallSum += (6 - smaller_sum_array[left])
            left += 1
            count += 1
            diff = largeSum - smallSum
            if diff <= 0:  # point where largeSum is going down => suggests that point where sum can be equal
                return count

        while right > 0:  # small_sum+array exhausted , only way is decrement in larget_sum_array
            largeSum -= (larger_sum_array[right] - 1)
            right -= 1
            count += 1
            diff = largeSum - smallSum
            if diff <= 0:  # point where largeSum is going down => suggests that point where sum can be equal
                return count

        return -1  # sorry , you could not make them equal```