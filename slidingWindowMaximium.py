# algorithm
from collections import deque

# we can keep track of the largest number in the window by using deque
# for example, if we have [1,2,3,4,3,2,1] in the window, we put each number into the deque sequentially
# [] -> [1] ->[1,2], when we find the previous number is smaller than current number, we pop it from the deque
# the logic behind it is that when we move the window from left to right, 2 is always in the window if 1 is in the window. so we don't need the information from 1.
# this process ensures that the first number is the largest in the window, the second is second largest(if exits)
# we have to do one more thing: pop the largest if the window passes


def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    l = deque([])
    for i in range(k):
        while l and nums[i] >= nums[l[-1]]:
            l.pop()
        l.append(i)
    ans = [nums[l[0]]]

    for i in range(1, len(nums)-k+1):
        while(l and nums[i+k-1] >= nums[l[-1]]):
            l.pop()
        l.append(i+k-1)
        if i-1 == l[0]:
            l.popleft()
        ans.append(nums[l[0]])
    return ans
