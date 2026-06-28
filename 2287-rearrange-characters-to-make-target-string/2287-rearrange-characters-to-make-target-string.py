class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter=defaultdict(int)
        for c in s:
            if c in target:
                counter[c]+=1
        if any(c not in counter for c in target):
            return 0
        req= defaultdict(int)
        for c in target:#since we dont have exact target word fixed over here, so we are storing the target word's frequency in this dictionary, and then later we wil devide it with the frequency of letter present in s.
            req[c]+=1
        return min(counter[c]//req[c] for c in req)