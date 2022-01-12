from typing import List


class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        # x=0                         O(n) ~ 72 ms
        # for i in nums:
        #     x^=i
        # return x
        if len(arr)==1:
            return arr[0]
        if arr[0]!=arr[1]:
            return arr[0]
        elif (arr[-1]!=arr[-2]):
            return arr[-1]
        else:
            low = 0
            high = len(arr)-1
            while low<=high:
                mid = (low+high)//2
                if arr[mid]==arr[mid-1] and arr[mid]!=arr[mid+1] and (mid-1)%2==0:
                    low = mid+1
                elif arr[mid]==arr[mid-1] and arr[mid]!=arr[mid+1] and (mid-1)%2!=0:
                    high = mid-1
                elif arr[mid]!=arr[mid-1] and arr[mid]==arr[mid+1] and mid%2==0:
                    low = mid+1
                elif arr[mid]!=arr[mid-1] and arr[mid]==arr[mid+1] and (mid)%2!=0:
                    high = mid-1
                else:
                    return arr[mid]