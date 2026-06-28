class Solution:
    def secondHighest(self, s: str) -> int:
        nums=[]
        for x in s:
            if x in ['0','1','2','3','4','5','6','7','8','9']:
                nums.append(int(x))
            
        largest=float("-inf")
        s_largest=float("-inf")
        for i in range(0,len(nums)):
            if nums[i] > largest:
                s_largest=largest
                largest=nums[i]
            elif nums[i] > s_largest and nums[i]!=largest:
                s_largest=nums[i]
        if s_largest == float("-inf"):
            return -1
        return s_largest


        