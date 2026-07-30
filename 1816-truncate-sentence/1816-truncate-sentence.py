class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        # words=s.split()
        # op=[]
        # i=0
        # if k==len(words):
        #     return s
        # while i<k:
        #     op.append(words[i])
        #     i+=1
        # return " ".join(op)
        words=s.split()
        res=[]
        i=0
        if len(words)==k:
            return s
        while i<k:
            res.append(words[i])
            i+=1
        return " ".join(res)






