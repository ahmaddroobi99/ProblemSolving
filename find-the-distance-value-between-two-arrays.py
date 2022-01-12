class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        count=0
        for x in arr1:
            l, r = 0, len(arr2)
            while l < r:
                mid = (l + r) // 2
                if abs(arr2[mid] - x) <= d:
                    count-=1
                    break
                elif arr2[mid] > x:
                    r = mid
                else:
                    l = mid + 1
            count+=1
        return count