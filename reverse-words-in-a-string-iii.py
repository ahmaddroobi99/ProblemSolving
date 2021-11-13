class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        temp_list = []
        for i in list_s:
            temp_list.append(i[::-1])
        return(" ".join(temp_list))