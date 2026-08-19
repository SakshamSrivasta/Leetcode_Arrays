class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dictt={}
        for c in arr:
            dictt[c]=dictt.get(c,0)+1
        ans=-1
        for key in dictt:
            if dictt[key]==key:
                ans=max(ans,key)
            
                
        return ans
        