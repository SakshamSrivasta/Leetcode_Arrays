class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictt={}
        for c in s:
            dictt[c]=dictt.get(c,0)+1
        if len(s)!=len(t):
            return False
        for c in t:
            if c not in dictt or dictt[c]==0:
                return False
            dictt[c]-=1
        return True
                    
