class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictt={}
        for c in nums:
            dictt[c]=dictt.get(c,0)+1
        majority=max(dictt.values())
        for key, value in dictt.items():
            if value == majority:
                return key
        return 0
        # for key,value in dictt:
        #     if dictt[value]==majority:
        #         return key
        #         break
        # return [key for key, value in dictt.items() if value == highest_value]
