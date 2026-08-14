class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dictt={}
        for c in nums:
            dictt[c]=dictt.get(c,0)+1
        for key in dictt:
            if dictt[key]==2:
                repeating_number=key
        n=len(nums)
        s1=n*(n+1)//2
        s2=sum(nums)
        return[repeating_number,(s1-s2)+repeating_number]

        
        
        
        
        
        
        
        
        
        
        
        
        # dictt={}
        # for c in nums:
        #     dictt[c]=dictt.get(c,0)+1
        # for key in dictt:
        #     if dictt[key]==2:
        #         repeating_number=key
        # n=len(nums)
        # s1=(n*(n+1))//2
        # s2=sum(nums)-repeating_number
        # return [repeating_number,s1-s2]


        #         dictt={}
        # for c in arr:
        #     dictt[c]=dictt.get(c,0)+1
        # for key in dictt:
        #     if dictt[key] == 2:
        #         repeating_number = key
        # n=len(arr)
        # sum2=n*(n+1)//2
        # sum1=sum(arr)-repeating_number
        # return [repeating_number,sum2-sum1]