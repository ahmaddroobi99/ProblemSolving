class Solution:
    def frequencySort(self, s: str) -> str:
        dic = {}
        result = []
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

        for k, v in dic:
            result.append(k * v)
        return "".join(result)