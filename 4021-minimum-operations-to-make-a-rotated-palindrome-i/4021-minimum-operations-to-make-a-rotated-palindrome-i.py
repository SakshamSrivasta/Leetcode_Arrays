class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        y=s
        ans=float('inf')
        for k in range(n):
            t=y[k:]+y[:k]
            cost=k
            for i in range(n//2):
                a=ord(t[i])-ord('a')
                b=ord(t[n-1-i])-ord('a')
                d=abs(a-b)
                cost+=min(d,26-d)
            ans=min(ans,cost)
        return ans