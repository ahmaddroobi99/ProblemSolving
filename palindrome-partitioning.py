class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(cur_s, cur_path):
            if not cur_s:
                self.ret.append(cur_path)
                return
            for i in range(1, len(cur_s) + 1):
                if cur_s[:i] == cur_s[:i][::-1]:
                    dfs(cur_s[i:], cur_path + [cur_s[:i]])

        self.ret = []
        dfs(s, [])
        return self.ret