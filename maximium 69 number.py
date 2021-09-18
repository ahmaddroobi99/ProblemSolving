

class Solution:
    def maximum69Number (self, num: int) -> int:
        string = str(num)
        string = string.replace('6','9',1)
        return int(string)