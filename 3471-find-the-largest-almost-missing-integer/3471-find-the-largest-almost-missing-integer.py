class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        dictt={}
        for c in nums:
            dictt[c]=dictt.get(c,0)+1
        if len(nums)==k:
            return max(nums)
        max_value=-1
        if k==1:
            for i in range(len(nums)):
                if dictt[nums[i]]==1 and nums[i]>max_value:
                    max_value=nums[i]
            return max_value
        n=len(nums)-1
        if nums[0]==nums[n]:
            return -1
        if dictt[nums[0]]==1 and dictt[nums[n]]==1:
            return max(nums[0],nums[n])
        if dictt[nums[0]]==1 and dictt[nums[n]]>1:
            return nums[0]
        if dictt[nums[0]]>1 and dictt[nums[n]]==1:
            return nums[n]
        return -1
        