class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        left = ret = numT = numF = 0

        for right in range(n):
            if answerKey[right] == 'T':
                numT += 1
            else:
                numF += 1
            while numT > k and numF > k:
                if answerKey[left] == 'T':
                    numT -= 1
                else:
                    numF -= 1
                left += 1
            ret = max(ret, right - left + 1)
        return ret
