class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_avg=0
        for i in range(k):
            window_avg+=nums[i]
        max_avg=window_avg
        for i in range(k,len(nums)):
            window_avg+=nums[i]
            window_avg-=nums[i-k]
            max_avg=max(max_avg,window_avg)
        return max_avg/k
        