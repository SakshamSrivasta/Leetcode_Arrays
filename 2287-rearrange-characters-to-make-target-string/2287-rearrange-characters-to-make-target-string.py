class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter=defaultdict(int)
        for c in s:
            if c in target:
                counter[c]+=1
        if any(c not in counter for c in target):
            return 0
        req= defaultdict(int)
        for c in target:
            req[c]+=1
        return min(counter[c]//req[c] for c in req)