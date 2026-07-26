import heapq
class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        def entry(i,j):
            return (i+1)*(j+1)
        INF=float('inf')
        size=m*n*2
        dist=[INF]*size
        def sid(i,j,p):
            return (i*n+j)*2 +p
        start =sid(0,0,1)
        dist[start]=entry(0,0)
        pq=[(dist[start],0,0,1)]
        moves=[
            (1,0,True),
            (0,1,True),
            (-1,0,False),
            (0,-1,False),
        ]
        target_i,target_j=m-1,n-1
        while pq:
            d,i,j,p=heapq.heappop(pq)
            if d>dist[sid(i,j,p)]:
                continue
            if i==target_i and j==target_j:
                return d
            pen=penalty[i][j]
            new_p=1-p
            wid=sid(i,j,new_p)
            nd=d+pen
            if nd<dist[wid]:
                dist[wid]=nd
                heapq.heappush(pq,(nd,i,j,new_p))
            for di,dj,is_right_down in moves:
                ni,nj=i+di,j+dj
                if 0<=ni <m and 0<=nj<n:
                    matches=(is_right_down and p==1) or (not is_right_down and p==0)
                    cost=entry(ni,nj)+(0 if matches else pen)
                    nid=sid(ni,nj,new_p)
                    nd2=d+cost
                    if nd2<dist[nid]:
                        dist[nid]=nd2
                        heapq.heappush(pq,(nd2,ni,nj,new_p))
        return min(dist[sid(target_i,target_j,0)],dist[sid(target_i,target_j,1)])