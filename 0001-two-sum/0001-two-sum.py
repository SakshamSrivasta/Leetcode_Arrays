class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt={}
        n=len(nums)
        for i in range(0,n):
            remaining=target - nums[i]
            if remaining in dictt:
                return [dictt[remaining],i]
            else:
                dictt[nums[i]]=i

        