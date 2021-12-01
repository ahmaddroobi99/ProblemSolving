class Solution:
    def hIndex(self, citations: List[int]) -> int:

        if len(citations) is 1 and citations[0] == 0 or sum(citations) == 0:
            return 0
        if len(citations) == 1:
            return 1

        def bs(start, end, array, lenArr):


            if end < start:
                return lenArr - start
            mid = (start + end) // 2
            if (lenArr - 1 - mid) + 1 == array[mid]:
                return lenArr - mid
            elif (lenArr - 1 - mid) + 1 > array[mid]:
                # right
                return bs(mid + 1, end, array, lenArr)
            elif (lenArr - 1 - mid) + 1 < array[mid]:
                # left
                return bs(start, mid - 1, array, lenArr)

        citations = sorted(citations)
        return (bs(0, len(citations) - 1, citations, len(citations)))