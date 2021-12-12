from collections import deque


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge(left_half, right_half):
            ret = []
            while left_half and right_half:
                # both left_half and right_half are sorted in DESCENDING order
                # if first element of left_half is greater than the first element
                # of right_half, it's greater than all elements in right_half.
                # we can therefore add len(right_half) to count[left_half[0][1]]
                if left_half[0][0] > right_half[0][0]:
                    # -----------------------------------------
                    self.count[left_half[0][1]] += len(right_half)
                    # -----------------------------------------
                    ret.append(left_half.popleft())
                else:
                    ret.append(right_half.popleft())

            if left_half:
                ret.extend(left_half)
            if right_half:
                ret.extend(right_half)
            return ret

        def mergeSort(A):
            if len(A) == 1:
                return A
            mid = len(A) // 2
            left_half = mergeSort(A[:mid])
            right_half = mergeSort(A[mid:])
            return merge(deque(left_half), deque(right_half))

        self.count = [0] * len(nums)
        nums = [(nums[i], i) for i in range(len(nums))]
        mergeSort(nums)
        return self.count