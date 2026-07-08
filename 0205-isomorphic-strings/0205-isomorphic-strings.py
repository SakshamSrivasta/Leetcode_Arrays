class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stot={}
        ttos={}
        for i in range(len(s)):
            char_s=s[i]
            char_t=t[i]
            if char_s in stot:
                if char_t!=stot[char_s]:
                    return False
            else:
                stot[char_s]=char_t
            if char_t in ttos:
                if char_s!=ttos[char_t]:
                    return False
            else:
                ttos[char_t]=char_s
        return True