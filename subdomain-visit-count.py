class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        for s in cpdomains:
            cnt, s = s.split()
            cnt = int(cnt)
            d[s] += cnt
            pos = s.find('.') + 1
            while pos > 0:
                d[s[pos:]] += cnt
                pos = s.find('.', pos) + 1
        for x, i in d.items():
            yield f'{i} {x}'