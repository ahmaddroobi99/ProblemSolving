class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        nodes = collections.defaultdict(set)
        emailsToName = {}
        for act in accounts:
            name = act[0]
            for i in range(1, len(act)):
                email = act[i]
                emailsToName[email] = name
                for j in range(1, len(act)):
                    if i != j:
                        email2 = act[j]
                        nodes[email].add(email2)

        seen = set()
        out = []

        def dfs(email, arr):
            if email not in seen:
                arr.append(email)
                seen.add(email)
            else:
                return
            for em in nodes[email]:
                dfs(em, arr)

        for em in emailsToName:
            if em not in seen:
                arr = []
                dfs(em, arr)
                arr.sort()
                arr.insert(0, emailsToName[em])
                out.append(arr)
        return out


