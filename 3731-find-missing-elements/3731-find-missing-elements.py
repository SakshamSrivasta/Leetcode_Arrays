class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        x=min(nums)
        y=max(nums)
        ans=[]
        present=set(nums)
        for i in range(x,y):
            if i not in present:
                ans.append(i)
        return ans       
