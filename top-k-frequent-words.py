class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hashmap = {}
        answer = []
        count = []

        if len(words)<1:
            return 0

        words = sorted(words)
        for i in range(len(words)):
            if words[i] in hashmap:
                hashmap[words[i]] +=1
            else:
                hashmap[words[i]] = 1


        sorted_h = sorted(hashmap.values(),reverse=True)

        for i in range(k):
            count.append(sorted_h[i])

        for i in count:
            for key,val in hashmap.items():
                if i == val and key not in answer and len(answer)<k:
                    answer.append(key)


        return answer