# Two
# pointer
nums1.sort()
nums2.sort()

one = 0
two = 0

p = set()

whlie:
   one < len(nums1) and two < len(nums2):

   if nums1[one] == nums2[two]:
    p.add(nums1[one])

    one += 1
    two += 1
elif nums1[one] > nums2[two]:
    two += 1
else:
    one += 1

return list(p)

# Hash
# map
f = {}
for i in nums1:
    if i not in f:
        f[i] = 1

result = set()

for j in nums2:
    if j in f:
        result.add(j)

return list(result)
#
# One
# liner

return set(nums1) & set(nums2)