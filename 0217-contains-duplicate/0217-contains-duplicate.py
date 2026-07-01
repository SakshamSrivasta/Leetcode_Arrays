class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt={}
        for x in nums:
            if x in dictt:
                return True
            dictt[x]=1
        return False
        