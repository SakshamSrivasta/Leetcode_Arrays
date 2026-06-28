class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt={}
        for i in range(0,len(nums)):
            remaining=target- nums[i]
            if remaining in dictt:
                return [dictt[remaining],i]
            dictt[nums[i]]=i


                

        