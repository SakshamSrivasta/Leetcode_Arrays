class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s=nums[0]
        l=nums[0]
        for i in range(len(nums)):
            if nums[i]<s:
                s=nums[i]
            if nums[i]>l:
                l=nums[i]
        while l != 0:
            s, l = l, s % l
        return s