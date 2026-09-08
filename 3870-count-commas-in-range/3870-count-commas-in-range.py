class Solution:
    def countCommas(self, n: int) -> int:
        if n>=1 and n<=999:
            return 0
        else:
            return n-999
        # count=0
        # for i in range(1,n+1):
        #     if i>999:
        #         count+=1
        # return count
