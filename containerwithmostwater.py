class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        allpairs = []
        value = 0
        left =0
        right = length -1
        for i in range(length):
            if height[left] > height[right]:
                value = (right - left) * height[right]
                allpairs.append(value)
                right -= 1
            else:
                value = (right - left) * height[left]
                allpairs.append(value)
                left += 1
        return max(allpairs)