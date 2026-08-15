class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:
        a=sorted(set(requests+[start]))
        x=(n,start,requests)
        m=len(a)
        s=a.index(start)
        q=len(requests)
        has_start=start in set(requests)
        INF=10**30
        L=[[INF]*m for _ in range(m)]
        R=[[INF]*m for _ in range(m)]
        L[s][s]=R[s][s]=0
        for length in range(1,m+1):
            for l in range(max(0,s-length+1),min(s,m-length)+1):
                r=l+length-1
                rem=q-(r-l)-has_start
                if l>0:
                    L[l-1][r]=min(
                        L[l-1][r],
                        L[l][r]+(a[l]-a[l-1])*rem,
                        R[l][r]+(a[r]-a[l-1])*rem
                    )
                if r+1<m:
                    R[l][r+1]=min(
                        R[l][r+1],
                        L[l][r]+(a[r+1]-a[l])*rem,
                        R[l][r]+(a[r+1]-a[r])*rem
                    )
        return min(L[0][m-1],R[0][m-1])