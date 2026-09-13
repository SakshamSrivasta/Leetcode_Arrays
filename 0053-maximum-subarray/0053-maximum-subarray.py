class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # maxi=float("-inf")
        # for i in range(0,len(nums)):
        #     total=0
        #     for j in range(i,len(nums)):
        #         total+=nums[j]
        #         maxi=max(total,maxi)
        # return maxi
        total=0
        maxi=float("-inf")
        for i in range(0,len(nums)):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi






        