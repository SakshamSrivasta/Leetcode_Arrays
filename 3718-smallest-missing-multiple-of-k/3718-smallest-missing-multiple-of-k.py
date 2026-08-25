class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        ans=k
        while ans in s:
            ans+=k
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        # if len(nums)==1:
        #     if nums[0]==k:
        #         return nums[0]*2
        #     else: 
        #         return k*1
        
        # for i in range(1,len(nums)+2):
        #     s=k*i
        #     if s not in nums:
        #         return s
        #         break
        