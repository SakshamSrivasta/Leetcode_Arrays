class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        sum1=sum(nums)
        sum2=0
        for i in range(0,n+1):
            sum2+=i
        return sum2-sum1