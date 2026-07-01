class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt={}
        for i in range(len(nums)):
            if nums[i] not in dictt:
                dictt[nums[i]]=1
            else:
                dictt[nums[i]]+=1
        for k in dictt:
            if dictt[k] >=2:
                return True
        return False
        