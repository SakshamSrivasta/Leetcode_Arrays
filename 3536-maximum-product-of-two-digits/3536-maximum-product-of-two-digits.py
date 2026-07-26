class Solution:
    def maxProduct(self, n: int) -> int:
        # first = 0
        # second = 0
        # while n>0:
        #     x=n%10
        #     if x>first:
        #         second,first=first,x
        #     elif x>second:
        #         second=x
        #     n//=10
        # return first*second
        ans=[]
        temp=n
        while temp>0:
            ans.append(temp%10)
            temp//=10
        ans.sort()
        return ans[-1]*ans[-2]