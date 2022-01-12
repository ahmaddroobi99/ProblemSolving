class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:

        frequency = {}
        for i in A.split():
            frequency[i] = frequency.get(i, 0) + 1
        for i in B.split():
            frequency[i] = frequency.get(i, 0) + 1

        answer = []
        for k, v in frequency.items():
            if v < 2: answer.append(k)
        return answer