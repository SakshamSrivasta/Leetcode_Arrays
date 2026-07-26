class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        MOD= 10**9 +7
        fact=[1]* (n+1)
        for i in range(1,n+1):
            fact[i]=fact[i-1] * i%MOD
        inv_fact = [1]*(n+1)
        inv_fact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1):
            inv_fact[i]=inv_fact[i+1]*(i+1)%MOD
        def comb(a:int,b:int)-> int:
            if b<0 or b>a or a<0:
                return 0
            return fact[a]* inv_fact[b] % MOD * inv_fact[a-b] %MOD
        total=comb(n-1,k-1)
        all_odd=0
        if(n-k)%2==0:
            m=(n-k)//2
            all_odd=comb(m+k-1,k-1)
        return (total-all_odd)%MOD