class Solution:
    def decodeString(self, s: str) -> str:
        # pay attention to numbers larger than 9
        if s.isalpha():
            return s
        n = len(s)
        count = left = 0
        num = -1
        ret = ''
        for i in range(n):
            if count==0 and s[i].isalpha():
                ret += s[i]
            elif s[i]=='[':
                count+=1
            elif count==0 and num==-1 and s[i].isnumeric():
                left = s.find('[',i)
                num = int(s[i:left])
            elif s[i]==']':
                count-=1
                if count==0:
                    ret += num*self.decodeString(s[left+1:i])
                    num = -1
        return ret